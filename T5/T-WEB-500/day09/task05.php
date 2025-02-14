<?php
function form_is_submitted() {
    return isset($_POST['submit']);
}

function whoami() {
    $name = empty($_POST['name']) ? null : $_POST['name'];
    $age = empty($_POST['age']) ? null : $_POST['age'];
    $curriculum = empty($_POST['curriculum']) ? null : $_POST['curriculum'];
    if ($curriculum !== null) {
        switch ($curriculum) {
            case "pge":
                $curriculum = "PGE (Programme Grande Ecole)";
                break;
            case "msc":
                $curriculum = "MSc Pro";
                break;
            case "coding":
                $curriculum = "Coding Academy";
                break;
            case "wac":
                $curriculum = "Web@cademie";
                break;
        }           
    }

    if ($name !== null && $age !== null && is_numeric($age)) {
        echo "Hi, my name is $name and I'm $age years old.";
        if ($curriculum !== null) {
            echo " I'm a student of $curriculum.";
        }
    } elseif ($name === null && $age !== null && is_numeric($age)) {
        echo "Hi, I have no name and I'm $age years old.";
        if ($curriculum !== null) {
            echo " I'm a student of $curriculum.";
        }
    } elseif ($name !== null && ($age === null || !is_numeric($age))) {
        echo "Hi, my name is $name.";
        if ($curriculum !== null) {
            echo " I'm a student of $curriculum.";
        }
    } else {
        echo "Hi, I have no name";
    }
}
?>
