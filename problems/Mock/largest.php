<?php

function findKLargestElement($nums, $k)
{
    $heap = new SplMinHeap();

    foreach (array_slice($nums, 0, $k) as $num) {
        $heap->insert($num);
    }

    for ($i = $k; $i < count($nums); $i++) {
        if ($nums[$i] > $heap->top()) {
            $heap->extract();
            $heap->insert($nums[$i]);
        }
    }

    return $heap->top();
}

print_r(findKLargestElement([3, 2, 1, 5, 6, 4], 2));
