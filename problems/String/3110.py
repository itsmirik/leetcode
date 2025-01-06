class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        for i in range(len(s) - 1):
            result += abs(ord(s[i]) - ord(s[i + 1]))

        return result


if __name__ == '__main__':
    s = 'hello'
    print(Solution().scoreOfString(s))  # 5
