class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = s.split(' ')
        result = ''
        n = len(split_s)

        for i in range(n - 1):
            extra_space = ''
            if i != n - 1:
                extra_space = ' '

            result = result + split_s[i][::-1] + extra_space

        return result


if __name__ == '__main__':
    print(Solution().reverseWords("Let's take LeetCode contest"))
