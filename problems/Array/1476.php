<?php

class SubrectangleQueries
{
    /**
     * @param Integer[][] $rectangle
     */
    function __construct(private array $rectangle)
    {

    }

    /**
     * @param Integer $row1
     * @param Integer $col1
     * @param Integer $row2
     * @param Integer $col2
     * @param Integer $newValue
     * @return NULL
     */
    function updateSubrectangle(int $row1, int $col1, int $row2, int $col2, int $newValue): null
    {
        for ($i = $row1; $i <= $row2; $i++) {
            for ($j = $col1; $j <= $col2; $j++) {
                $this->rectangle[$i][$j] = $newValue;
            }
        }

        return null;
    }

    /**
     * @param Integer $row
     * @param Integer $col
     * @return Integer
     */
    function getValue(int $row, int $col): int
    {
        return $this->rectangle[$row][$col];
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * $obj = SubrectangleQueries($rectangle);
 * $obj->updateSubrectangle($row1, $col1, $row2, $col2, $newValue);
 * $ret_2 = $obj->getValue($row, $col);
 */

$solution = new SubrectangleQueries(
    [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
);
$solution->updateSubrectangle(3, 0, 3, 2, 10);
//print_r($solution->updateSubrectangle(0, 0, 3, 2, 5));
