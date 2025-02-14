<?php
function calc(string $operator, int $nbr1, int $nbr2) {
    if ($operator === "+") {
        return $nbr1+$nbr2;
    }
    if ($operator === "-") {
        return $nbr1-$nbr2;
    }
    if ($operator === "*") {
        return $nbr1*$nbr2;
    }
    if ($nbr2 === 0) {
        return "Cannot divide by 0";
    }
    if ($operator === "/") {
        return $nbr1/$nbr2;
    }
    if ($operator === "%") {
        return $nbr1%$nbr2;
    }
    return "Unknown operator";
}
?>
