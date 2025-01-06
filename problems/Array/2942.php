<?php

class Solution
{

    /**
     * @param String[] $words
     * @param String $x
     * @return Integer[]
     */
    function findWordsContaining($words, $x)
    {
        $indexesWordWithX = [];

        foreach ($words as $key => $word) {
            if (str_contains($word, $x)) {
                $indexesWordWithX[] = $key;
            }
        }

        return $indexesWordWithX;
    }
}

$solution = new Solution();
print_r($solution->findWordsContaining(["leet", "code"], 'e'));