<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Web login access control examples</title>
        <link rel="stylesheet" href="bootstrap.min.css">
    </head>
    <body class="p-1">
        <div class="container">
        <h2><a href="v1" target="_blank">v1: storing usernames and passwords (in plaintext) -- BAD!</a></h2>
        <h2><a href="v2" target="_blank">v2: storing usernames and encrypted passwords (with a symmetric key) -- BAD!</a></h2>
        <h2><a href="v3" target="_blank">v3: storing usernames and hashed passwords (with a one-way hash function) -- MEH</a></h2>
        <h2><a href="v4" target="_blank">v4: adding salt -- GOOD</a></h2>
        <h2><a href="v5" target="_blank">v5: using hash stretching -- BEST</a></h2>
    </body>
</html>
