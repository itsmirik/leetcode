<?php

class Solution
{

    /**
     * @param Integer[][] $accounts
     * @return Integer
     */
    function maximumWealth(array $accounts): int
    {
        $total = 0;
        foreach ($accounts as $account) {
            if ($total < array_sum($account)) {
                $total = array_sum($account);
            }
        }

        return $total;
    }
}

$solution = new Solution();
//print_r($solution->maximumWealth([[1, 2, 3], [3, 2, 1]]));
print_r($solution->maximumWealth([[1, 5], [7, 3], [3, 5]]));
