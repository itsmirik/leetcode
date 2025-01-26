class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left, right = 0, len(s) - 1
        result = list(s)

        # print(ord('a'), ord('b')) 97, 98
        while left < right:
            if s[left] != s[right]:
                if ord(s[left]) < ord(s[right]):
                    result[right] = s[left]
                else:
                    result[left] = s[right]
            left += 1
            right -= 1

        return ''.join(result)


if __name__ == '__main__':
    # print(Solution().makeSmallestPalindrome("egcfe"))
    print(Solution().makeSmallestPalindrome("abcd"))
