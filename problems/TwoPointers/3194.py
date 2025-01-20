from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        return min((nums[i] + nums[~i]) / 2 for i in range(len(nums) // 2))

if __name__ == '__main__':
    print(Solution().minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]))
