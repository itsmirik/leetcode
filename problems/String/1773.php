<?php

class Solution
{

    /**
     * @param String[][] $items
     * @param String $ruleKey
     * @param String $ruleValue
     * @return Integer
     */
    function countMatches(array $items, string $ruleKey, string $ruleValue)
    {
        $rules = [
            'type'  => 0,
            'color' => 1,
            'name'  => 2,
        ];
        $count = 0;
        for ($i = 0; $i < count($items); $i++) {
            if ($items[$i][$rules[$ruleKey]] === $ruleValue) {
                $count++;
            }
        }

        return $count;
    }
}

$solution = new Solution();
print_r($solution->countMatches(
    [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
    "color",
    "silver"
));

print_r($solution->countMatches(
    [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
    "type",
    "phone"
));