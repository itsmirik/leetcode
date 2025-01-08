class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y = int(date[0:4])
        m = int(date[5:7])
        d = int(date[8:10])

        def to_binary(n):
            if n == 0:
                return '0'
            bin_str = ''
            while n > 0:
                bin_str = str(n % 2) + bin_str
                n //= 2
            return bin_str

        yb = to_binary(y)
        mb = to_binary(m)
        db = to_binary(d)

        ans = yb + '-' + mb + '-' + db
        return ans


if __name__ == '__main__':
    print(Solution().convertDateToBinary("2080-02-29"))
