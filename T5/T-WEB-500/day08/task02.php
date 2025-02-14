<?php
function dog_bark(int $woof_nb) {
    if ($woof_nb > 0) {
        for ($n = 0; $n < $woof_nb; $n++) {
            echo "woof";
            if ($n < $woof_nb-1) {
                echo " ";
            }
        }
    }
    echo PHP_EOL;
}
?>
