from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than_pivot = []
        greater_than_pivot = []
        equal_to_pivot = []

        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)

            if num > pivot:
                greater_than_pivot.append(num)

            if num == pivot:
                equal_to_pivot.append(num)

        return less_than_pivot + equal_to_pivot + greater_than_pivot

if __name__ == '__main__':
    print(Solution().pivotArray([9, 12, 5, 10, 14, 3, 10], 10))
