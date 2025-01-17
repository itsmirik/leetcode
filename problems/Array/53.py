class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0

        for num in nums:
            currentSum += num

            if currentSum > maxSum:
                maxSum = currentSum

            if currentSum < 0:
                currentSum = 0

        return maxSum


if __name__ == '__main__':
    s = 'hello'
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
