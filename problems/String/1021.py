class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result, count = '', 0

        for c in s:
            if c == ')': count -= 1
            if count != 0: result += c
            if c == '(': count += 1

        return result


if __name__ == '__main__':
    print(Solution().removeOuterParentheses("(()())(())"))
