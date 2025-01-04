<?php

class Solution
{

    /**
     * @param Integer[] $candies
     * @param Integer $extraCandies
     * @return Boolean[]
     */
    function kidsWithCandies(array $candies, int $extraCandies): array
    {
        $result = [];
        $max    = max($candies);

        foreach ($candies as $candy) {
            $result[] = $candy + $extraCandies >= $max;
        }

        return $result;
    }
}

$solution = new Solution();
print_r($solution->kidsWithCandies([2, 3, 5, 1, 3], 3));