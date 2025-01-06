<?php

class Solution
{

    /**
     * @param String $s
     * @param Integer[] $indices
     * @return String
     */
    function restoreString(string $s, array $indices)
    {
        $restoredString = '';

        for ($i = 0; $i < strlen($s); $i++) {
            $restoredString[$indices[$i]] = $s[$i];
        }

        return $restoredString;
    }
}

$solution = new Solution();
print_r($solution->restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]));
print_r($solution->restoreString("abc", [0,1,2]));
