class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = len(word1) - 1, len(word2) - 1
        result = []

        while i >= 0 or j >= 0:
            if i > j:
                result.append(word1[i])
                i -= 1
            else:
                result.append(word2[j])
                j -= 1

        return ''.join(result[::-1])

if __name__ == '__main__':
    print(Solution().mergeAlternately('ab', 'pqrs'))
