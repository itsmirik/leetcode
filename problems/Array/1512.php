<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numIdenticalPairs($nums)
    {
        $result = 0;
        $l = count($nums);
        for ($i = 0; $i < $l; $i++) {
            for ($j = $i + 1; $j < $l; $j++) {
                if ($nums[$i] === $nums[$j]) {
                    $result++;
                }
            }
        }

        return $result;
    }
}

$solution = new Solution();
//print_r($solution->numIdenticalPairs([1, 2, 3, 1, 1, 3]));
//print_r($solution->numIdenticalPairs([1, 1, 1, 1]));
print_r($solution->numIdenticalPairs([1, 2, 3]));