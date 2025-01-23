class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, 0
        temp = ''

        while right < len(s):
            if s[right] != ' ':
                right += 1
            elif s[right] == ' ':
                temp += s[left:right + 1][::-1]
                right += 1
                left = right

        temp += ' '
        temp += s[left:right + 2][::-1]
        return temp[1:]


if __name__ == '__main__':
    # print(Solution().reverseWords("Let's take LeetCode contest"))
    print(Solution().reverseWords("Mr Ding"))
