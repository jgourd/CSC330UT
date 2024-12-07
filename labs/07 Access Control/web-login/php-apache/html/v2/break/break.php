<?php

$DICTIONARY = "words.txt";

// enter the DB password below
$db_password = "0Iw5SIdDykdW0iqH5GIzsA==";

// grab the dictionary words
$words = file($DICTIONARY, FILE_IGNORE_NEW_LINES);

foreach ($words as $password)
{
    echo "Trying: $password on $db_password: ";

    // decrypt the password with the known symmetric key
    $plain_password = openssl_decrypt($db_password, "aes-256-cbc", $password);

    // display the results
    echo "$plain_password\n";
}

?>
