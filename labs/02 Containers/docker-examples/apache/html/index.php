<html>
    <head>
        <title>My first web site!</title>
    </head>
    <body>
        <h1>Hello world!</h1>

        <p>It works!</p>
<?php

    echo "\t\t<p>Cool! It also works in PHP!</p>\n";
    
    date_default_timezone_set("America/New_York");
    $date = date("D d M Y", time());
    $time = date("h:i:s a", time());

    echo "\t\t<h2>Today is $date. It is now $time.</h2>\n";

?>
        <p>(refresh me)</p>
    </body>
</html>
