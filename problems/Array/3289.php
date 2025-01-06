<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function getSneakyNumbers(array $nums)
    {
        sort($nums);
        $result = [];

        for ($i = 0; $i < count($nums) - 1; $i++) {
            if ($nums[$i] === $nums[$i+1]) {
                $result[] = $nums[$i];
            }
        }

        return $result;
    }

    /*function getSneakyNumbers(array $nums)
    {
        $arr    = array_count_values($nums);
        $result = [];

        foreach ($arr as $key => $value) {
            if ($value > 1) {
                $result[] = $key;
            }
        }

        return $result;
    }*/
}

$solution = new Solution();
print_r($solution->getSneakyNumbers([0, 1, 1, 0]));
//print_r($solution->getSneakyNumbers([0, 3, 2, 1, 4, 3, 2]));
//print_r($solution->getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]));
