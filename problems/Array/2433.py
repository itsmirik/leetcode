from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        prev_value = pref[0]

        for i in range(0, len(pref)):
            if i != 0:
                xor = pref[i] ^ prev_value
                prev_value = pref[i]
                pref[i] = xor

        return pref


if __name__ == '__main__':
    print(Solution().findArray([5, 2, 0, 3, 1]))
