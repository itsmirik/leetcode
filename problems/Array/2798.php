<?php

class Solution
{

    /**
     * @param Integer[] $hours
     * @param Integer $target
     * @return Integer
     */
    function numberOfEmployeesWhoMetTarget(array $hours, int $target)
    {
        $total = 0;
        foreach ($hours as $hour) {
            if ($hour >= $target) {
                $total++;
            }
        }

        return $total;
    }
}

$solution = new Solution();
print_r($solution->numberOfEmployeesWhoMetTarget([0, 1, 2, 3, 4], 2));
//print_r($solution->numberOfEmployeesWhoMetTarget([5, 1, 4, 2, 2], 6));
