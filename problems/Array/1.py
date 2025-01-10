class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result: dict = {}

        for key, num in enumerate(nums):
            request = target - num

            if request in result:
                return [result[request], key]

            result[num] = key

        return []


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
