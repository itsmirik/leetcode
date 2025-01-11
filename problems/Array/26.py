from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        iterator = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[iterator]:
                iterator += 1
                nums[iterator] = nums[j]

        return iterator + 1


'''
Approach: j == i - 1 ? do nothing : move j into i th place
i = j = 1
0 0 1 1 1 2 2 3 3 4
  i
  j
if nums[j] == nums[i - 1] 0 == 0: do nothing
i = 1 j = 2

0 0 1 1 1 2 2 3 3 4
  i j
if 1 == 0: put j in i th place
0 1 1 1 1 2 2 3 3 4
    i j
i = 2 j = 3
if 1 == 1: do nothing
0 1 1 1 1 2 2 3 3 4
    i   j
i = 2 j = 4
if 4 == 1: do nothing
0 1 1 1 1 2 2 3 3 4
    i     j
i = 2 j = 5
if 2 == 1: put j in i th place
0 1 2 1 1 2 2 3 3 4
      i     j
'''

if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 2]))
