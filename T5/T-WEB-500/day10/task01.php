<?php
header('Content-Type: application/json'); // Specify JSON response header
if (isset($_GET['name'])) {
    $name = $_GET['name'];
    echo json_encode(['name' => $name]);
} else {
    echo json_encode(['error' => 'Name not provided']);
}
?>
