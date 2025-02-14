<?php
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $_POST['email'];

    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo json_encode(['message' => 'Email address is valid']);
    } else {
        http_response_code(400); // Set HTTP status code to 400 Bad Request
        echo json_encode(['message' => 'Email address is not valid']);
    }
} else {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed (not POST method)']);
}
// curl -d "name=Jane&email=john.doe@example.com" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://127.0.0.1/web_day10/task02.php
?>
