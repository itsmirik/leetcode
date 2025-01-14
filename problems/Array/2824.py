class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1

        return count


if __name__ == '__main__':
    # print(Solution().countPairs([-6, 2, 5, -2, -7, -1, 3], -2))
    print(Solution().countPairs([9, -5, -5, 5, -5, -4, -6, 6, -6], 3))
    # print(Solution().countPairs([-1, 1, 2, 3, 1], 2))
