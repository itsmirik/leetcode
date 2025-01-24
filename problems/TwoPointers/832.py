from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]

            for j in range(len(image[i])):
                image[i][j] = image[i][j] ^ 1

        return image

        # n = len(image)
        # i, j, k = 0, 0, n
        #
        # while k != 0:
        #     left, right = 0, len(image[i]) - 1
        #     while left <= right:
        #         temp = image[i][left] ^ 1
        #         # print(image[i][left], temp)
        #         print(left, right, k)
        #         image[i][left] = image[i][right] ^ 1
        #         image[i][right] = temp
        #         left += 1
        #         right -= 1
        #
        #     k -= 1
        #
        # return image


if __name__ == '__main__':
    print(Solution().flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
