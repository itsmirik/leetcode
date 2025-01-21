from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        count = 0
        if n < 3:
            return count

        seen = []

        for num in nums:
            if num - diff in seen and num - 2 * diff in seen:
                count += 1

            seen.append(num)

        return count


if __name__ == '__main__':
    print(Solution().arithmeticTriplets([0, 1, 4, 6, 7, 10], 3))
    # print(Solution().arithmeticTriplets([4, 5, 6, 7, 8, 9], 2))
