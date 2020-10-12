class Solution:
    def solve(self, matrix):
        def go(x, y):
            r = 4
            if x > 0:
                r -= matrix[x - 1][y]
            if x + 1 < len(matrix):
                r -= matrix[x + 1][y]
            if y > 0:
                r -= matrix[x][y - 1]
            if y + 1 < len(matrix[0]):
                r -= matrix[x][y + 1]

            return r
        ans = 0
        for i, x in enumerate(matrix):
            for j, y in enumerate(x):
                if matrix[i][j]:
                    ans += go(i, j)

        return ans
