class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0

        while left < right:
            if nums[left] + nums[right] < target:
                count += (right - left)
                left += 1
            else:
                right -= 1

        return count


if __name__ == '__main__':
    # print(Solution().countPairs([-6, 2, 5, -2, -7, -1, 3], -2))
    print(Solution().countPairs([9, -5, -5, 5, -5, -4, -6, 6, -6], 3))
    # print(Solution().countPairs([-1, 1, 2, 3, 1], 2))
