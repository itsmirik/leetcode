class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        invalid = 0

        for word in words:
            for w in word:
                if w not in allowed:
                    invalid += 1
                    break

        return len(words) - invalid

if __name__ == '__main__':
    print(Solution().countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
