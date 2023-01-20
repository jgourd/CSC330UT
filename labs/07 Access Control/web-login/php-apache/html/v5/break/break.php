<?php

$DICTIONARY = "words.txt";

// enter the DB hash below
$db_hash = "";

// grab the dictionary words
$words = file($DICTIONARY, FILE_IGNORE_NEW_LINES);

// hash each dictionary word and compare
foreach ($words as $password)
{
    echo "Trying: $password\n";
    if (password_verify($password, $db_hash))
    {
        // we found it!
        echo "**SUCCESS!\n";
        break;
    }
}

?>

