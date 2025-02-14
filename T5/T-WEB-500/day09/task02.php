<?php
function render_body(string $page) {
    switch($page) {
        case "home":
            return file_get_contents("home.html");
        case "sql":
            return file_get_contents("sql.html");
        case "php":
            return file_get_contents("php.html");
    }
    return '<p>Unknown page</p>';
}
?>
