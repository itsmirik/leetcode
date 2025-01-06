<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum(array $nums, int $target)
    {
        $result = [];

        foreach ($nums as $key => $num) {
            $diff = $target - $num; // 9 - 2 => 7 |||| 9 - 7 = 2

            if (isset($result[$diff])) {
                return [$result[$diff], $key];
            }

            $result[$num] = $key; // [7: 0] |||| [2: 1]
        }

        return null;
    }
}

$solution = new Solution();
print_r($solution->twoSum([2, 7, 11, 15], 9));
//print_r($solution->twoSum([3, 2, 4], 6));