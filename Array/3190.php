<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumOperations($nums)
    {
        $l = count($nums);
        $c = 0;
        for ($i = 0; $i < $l; $i++) {
            if (($nums[$i] - 1) % 3 === 0 || ($nums[$i] + 1) % 3 === 0) {
                $c++;
            }
        }

        return $c;
    }
}

$solution = new Solution();
print_r($solution->minimumOperations([1, 2, 3, 4]));