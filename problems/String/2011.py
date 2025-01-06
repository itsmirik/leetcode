from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for operation in operations:

            if operation == '--X' or operation == 'X--':
                result -= 1

            if operation == '++X' or operation == 'X++':
                result += 1

        return result


if __name__ == '__main__':
    print(Solution().finalValueAfterOperations(["--X", "X++", "X++"]))
