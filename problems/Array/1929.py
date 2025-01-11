class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums

if __name__ == '__main__':
    print(Solution().getConcatenation([1, 2, 1]))
