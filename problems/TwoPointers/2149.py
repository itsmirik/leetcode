from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = []
        pos, neg = 0, 1

        for num in nums:
            if num >= 0:
                result.insert(pos, num)
                pos += 2
            else:
                result.insert(neg, num)
                neg += 2

        return result


if __name__ == '__main__':
    print(Solution().rearrangeArray([3, 1, -2, -5, 2, -4]))
