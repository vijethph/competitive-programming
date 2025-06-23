# https://leetcode.com/problems/spiral-matrix-ii/description/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]

        left, right = 0, n - 1
        top, bottom = 0, n - 1
        val = 1

        while left <= right:
            # fill every val in top row
            for c in range(left, right + 1):
                mat[top][c] = val
                val += 1
            top += 1

            # fill every val in right col
            for r in range(top, bottom + 1):
                mat[r][right] = val
                val += 1
            right -= 1

            # fill every val in bottom row (reverse order)
            for c in range(right, left - 1, -1):
                mat[bottom][c] = val
                val += 1
            bottom -= 1

            # fill every val in left col (reverse order)
            for r in range(bottom, top - 1, -1):
                mat[r][left] = val
                val += 1
            left += 1

        return mat