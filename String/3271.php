<?php

class Solution
{

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function stringHash(string $s, int $k)
    {
        $sortedAbs = 'abcdefghijklmnopqrstuvwxyz';
        $result    = '';
        $optLen    = strlen($s) / $k;
        for ($i = 0; $i < $optLen; $i++) {
            $str   = substr($s, 0, $k);
            $s     = substr($s, $k);
            $total = 0;
            for ($j = 0; $j < strlen($str); $j++) {
                $total += strpos($sortedAbs, $str[$j]);
            }
            $remain = $total % strlen($sortedAbs);
            $result .= $sortedAbs[$remain];
        }

        return $result;
    }
}

$solution = new Solution();
//print_r($solution->stringHash('abcd', 2));
print_r($solution->stringHash('mxz', 3));
