<?php

class Solution
{

    /**
     * @param String $word
     * @param String $ch
     * @return String
     */
    function reversePrefix($word, $ch)
    {
        $reversedStr = '';
        $leftStr     = '';

        if (!$ch || $word === $ch) {
            return $word;
        }

        for ($i = 0; $i < strlen($word); $i++) {
            if ($word[$i] === $ch) {
                $reversedLength = $i + 1;
                $reversedStr    = strrev(substr($word, 0, $i + 1));
                if (strlen($word) !== $reversedLength) {
                    $leftStr = substr($word, $reversedLength - strlen($word));
                }

                break;
            } else {
                return $word;
            }
        }

        return $reversedStr . $leftStr;
    }
}

$solution = new Solution();
$word     = "abcd";
$ch       = "z";

echo $solution->reversePrefix($word, $ch);