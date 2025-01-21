from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        count = 0
        if n < 3:
            return count

        nums_map = {}
        for key, num in enumerate(nums):
            nums_map[num] = key

        for num in nums:
            if num + diff in nums_map and num - diff in nums_map:
                count += 1

        return count


if __name__ == '__main__':
    print(Solution().arithmeticTriplets([0, 1, 4, 6, 7, 10], 3))
    # print(Solution().arithmeticTriplets([4, 5, 6, 7, 8, 9], 2))
