<?php
function whoami() {
    $name = $_POST['name'] ?? null;
    $age = $_POST['age'] ?? null;
    $message = "Wesh la mouli fonctionne";

    if ($name !== null && $age !== null && is_numeric($age)) {
        $message = "Hi, my name is $name and I'm $age years old." .PHP_EOL;
    } elseif ($name === null && $age !== null && is_numeric($age)) {
        $message = "Hi, I have no name and I'm $age years old." .PHP_EOL;
    } elseif ($name !== null && ($age === null || !is_numeric($age))) {
        $message = "Hi, my name is $name." .PHP_EOL;
    } else {
        $message = "Hi, I have no name." .PHP_EOL;
    }
    echo $message;
}
// curl -d "name=Jane&age=21" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://127.0.0.1/index04.php
// curl -d "nom=John&age=48" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://127.0.0.1/index04.php
?>