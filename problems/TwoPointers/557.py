class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = s.split(' ')

        for i in range(len(split_s)):
            if i == len(split_s) - 1:
                split_s[i] = split_s[i][::-1]
            else:
                split_s[i] = split_s[i][::-1] + ' '

        return ''.join(split_s)


if __name__ == '__main__':
    print(Solution().reverseWords("Let's take LeetCode contest"))
