<?php

error_reporting(E_ALL & ~E_WARNING & ~E_NOTICE);

// initialize the session
session_start();
 
// unset all of the session variables
$_SESSION = array();
 
// destroy the session.
session_destroy();
 
// redirect to the login page
header("location: login.php");
exit;

?>
