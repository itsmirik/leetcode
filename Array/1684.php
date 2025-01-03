<?php

class Solution
{
    function countConsistentStrings(string $allowed, array $words): int
    {
        $count = 0;
        foreach ($words as $word) {
            $isLegal = true;
            for ($i = 0; $i < strlen($word); $i++) {
                if (!str_contains($allowed, $word[$i])) {
                    $isLegal = false;
                    break;
                }
            }
            if ($isLegal) {
                $count++;
            }
        }

        return $count;
    }
}

$solution = new Solution();
print_r($solution->countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]));
