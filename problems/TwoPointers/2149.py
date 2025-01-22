from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_arr = []
        neg_arr = []

        result = []

        for num in nums:
            if num >= 0:
                pos_arr.append(num)
            else:
                neg_arr.append(num)

        for i in range(len(nums) // 2):
            result.insert(2 * i, pos_arr[i])
            result.insert(2 * i + 1, neg_arr[i])

        return result


if __name__ == '__main__':
    print(Solution().rearrangeArray([3, 1, -2, -5, 2, -4]))
