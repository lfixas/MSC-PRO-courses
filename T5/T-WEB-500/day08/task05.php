<?php
function calc_average(array $numbers) {
    if (empty($numbers)) {
        return 0;
    }
    return round(array_sum($numbers)/count($numbers),1);
}
?>
