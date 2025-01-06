<?php

class Solution
{

    /**
     * @return Integer
     */
    function numberOfBeams(array $bank)
    {
        $count = 0;
        $index = 0;

        foreach (str_ireplace(0, '', $bank) as $floor) {
            if (strlen($floor) === 0) {
                continue;
            }
            $count = $count + strlen($floor) * $index;
            $index = strlen($floor);
        }

        return $count;
    }
}

$solution = new Solution();

print_r($solution->numberOfBeams(["011001", "000000", "010100", "001000"]));