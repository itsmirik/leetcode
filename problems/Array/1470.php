<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @param Integer $n
     * @return Integer[]
     */
    function shuffle($nums, $n)
    {
        $arr1 = array_slice($nums, 0 ,$n);
        $arr2 = array_slice($nums, $n);
        $res = [];
        for ($i = 0; $i < $n; $i++) {
            $res[] = $arr1[$i];
            $res[] = $arr2[$i];
        }

        return $res;
    }
}

$solution = new Solution();
print_r($solution->shuffle([2, 5, 1, 3, 4, 7], 3));