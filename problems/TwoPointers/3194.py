from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        left, right = 0, len(nums) - 1
        sorted_nums = sorted(nums)
        min_avg = (sorted_nums[left] + sorted_nums[right]) / 2

        while left < right:
            calc = (sorted_nums[left] + sorted_nums[right]) / 2

            if calc < min_avg:
                min_avg = calc

            left += 1
            right -= 1

        return min_avg


if __name__ == '__main__':
    print(Solution().minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]))
    # print(Solution().minimumAverage([1, 9, 8, 3, 10, 5]))
    # print(Solution().minimumAverage([1, 2, 3, 7, 8, 9]))
