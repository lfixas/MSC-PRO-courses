<?php
function display_menu() {
    $menu = '<ul>' .PHP_EOL;
    $menu .= '<li><a href="home.php">Home</a></li>' .PHP_EOL;
    $menu .= '<li><a href="product.php">Products</a></li>' .PHP_EOL;
    $menu .= '<li><a href="about.php">About Us</a></li>' .PHP_EOL;
    $menu .= '<li><a href="contact.php">Contact</a></li>' .PHP_EOL;
    $menu .= '</ul>' .PHP_EOL;
    return $menu;
}
?>
