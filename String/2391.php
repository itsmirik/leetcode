<?php

class Solution
{

    /**
     * @param String[] $garbage
     * @param Integer[] $travel
     * @return Integer
     */
    function garbageCollection(array $garbage, array $travel): int
    {
        $sum = 0;
        $mul = 0;
        $p   = 0;
        $g   = 0;
        $m   = 0;

        for ($i = count($garbage) - 1; $i > 0; $i--) {
            $sum += strlen($garbage[$i]);

            if ($mul < 3) {
                for ($j = 0; $j < strlen($garbage[$i]); $j++) {
                    $ch = $garbage[$i][$j];
                    switch ($ch) {
                        case 'P':
                            $mul = $p == 0 ? $mul + 1 : $mul;
                            $p++;
                            break;
                        case 'G':
                            $mul = $g == 0 ? $mul + 1 : $mul;
                            $g++;
                            break;
                        case 'M':
                            $mul = $m == 0 ? $mul + 1 : $mul;
                            $m++;
                            break;
                        default:
                            break;
                    }
                }
            }

            $sum += $mul * $travel[$i - 1];
        }

        $sum += strlen($garbage[0]);

        return $sum;
    }
}

$solution = new Solution();

print_r($solution->garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]));