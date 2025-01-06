<?php

class Solution
{

    /**
     * @param String[] $names
     * @param Integer[] $heights
     * @return String[]
     */
    function sortPeople(array $names, array $heights): array
    {
        /*second attempt
        $arrayCombine = array_combine($heights, $names);
        krsort($arrayCombine);
        return array_values($arrayCombine);*/

        $users = [];

        arsort($heights);
        $keys = array_keys($heights);

        for ($i = 0; $i < count($names); $i++) {
            $users[$i] = $names[$keys[$i]];
        }

        ksort($users);

        return $users;
    }
}

$solution = new Solution();
print_r($solution->sortPeople(["Mary", "John", "Emma"], [180, 165, 170]));
print_r($solution->sortPeople(
    [
        "GXLVEHVABFOGSFXUYYR",
        "TUHxnsxmu",
        "X",
        "OOYBLVKmzlaeaxbprc",
        "ARNLAPtfvmutkfsa",
        "XPMKPDUWOQEEILtbdjip",
        "QICEutjbr",
        "R",
    ],
    [11578, 89340, 73785, 12096, 55734, 89484, 59775, 72652]
));
