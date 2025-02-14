<?php
function sequence($n) {
    if ($n < 0) {
        return;
    }

    $seq = "1";
    echo $seq . PHP_EOL;

    for ($iter = 1; $iter <= $n; $iter++) {
        $newSeq = "";
        $len = strlen($seq);
        $elePos = 0;
        while ($elePos < $len) {
            $eleNumber = 1;
            while (($elePos + 1 < $len) && ($seq[$elePos] === $seq[$elePos + 1])) {
                $eleNumber++;
                $elePos++;
            }
            $newSeq .= $eleNumber . $seq[$elePos];
            $elePos++;
        }
        $seq = $newSeq;
        echo $seq . PHP_EOL;
    }
}
?>
