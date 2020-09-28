class Solution:
    def solve(self, matrix):
        # Write your code here
        for i in range(len(matrix)):
            for j in range(1, len(matrix[i])):
                matrix[i][j] += matrix[i][j - 1]

        for i in range(1, len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] += matrix[i - 1][j]

        return matrix
            
