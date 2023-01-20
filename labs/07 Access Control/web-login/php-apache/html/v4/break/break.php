<?php

$DICTIONARY = "words.txt";

// enter the DB hash below
$db_password = "";
// enter the DB salt below
$db_salt = "";

// grab the dictionary words
$words = file($DICTIONARY, FILE_IGNORE_NEW_LINES);

// hash each dictionary word and compare
foreach ($words as $password)
{
    echo "Trying: $password\n";
    if (hash("sha256", hex2bin($db_salt) . $password) == $db_password)
    {
        // we found it!
        echo "**SUCCESS!\n";
        break;
    }
}

?>

