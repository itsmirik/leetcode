<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function buildArray(array $nums)
    {
        $l=count($nums);
        $a=[];
        for($i=0;$i<$l;$i++){$a[]=$nums[$nums[$i]];}
        return $a;
    }
}

$solution = new Solution();
//print_r($solution->buildArray([0, 2, 1, 5, 3, 4]));
print_r($solution->buildArray([5, 0, 1, 2, 3, 4]));