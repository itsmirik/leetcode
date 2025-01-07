class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0

        for jewel in jewels:
            for stone in stones:
                if stone == jewel:
                    total += 1

        return total

if __name__ == '__main__':
    s = 'hello'
    print(Solution().numJewelsInStones("aA", "aAAbbbb"))
