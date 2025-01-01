<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function getConcatenation($nums)
    {
        return array_merge($nums, $nums);
    }
}

$solution = new Solution();
print_r($solution->getConcatenation([1,2,1]));