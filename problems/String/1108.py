class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))


if __name__ == '__main__':
    print(Solution().defangIPaddr("1.1.1.1"))
