<?php

class Solution
{

    /**
     * @param String $key
     * @param String $message
     * @return String
     */
    function decodeMessage($key, $message)
    {
        $sortedAbs = 'abcdefghijklmnopqrstuvwxyz';
        $opt       = '';
        $newKey    = '';

        return preg_replace(`/(.)\1+/g`, '$1', $key);
        return implode(',', explode(',', str_replace(' ', '', $key)));
//        for ($i = 0; $i < strlen(str_replace(' ', '', $key)); $i++) {
//
//        }

//        return implode(',', array_unique());
    }
}

$solution = new Solution();
print_r($solution->decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"));