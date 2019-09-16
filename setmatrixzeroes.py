class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        n = len(matrix)
        m = len(matrix[0])

        row = [0]*n
        col = [0]*m

        for i in range(n):
            for j in range(m):
                val = matrix[i][j]
                if val == 0:
                    print(i,j)
                    row[i] = 1
                    col[j] = 1

        for k in range(n):
            if row[k] == 1:
                for l in range(m):
                    matrix[k][l] = 0

        for a in range(m):
            if col[a] == 1:
                for b in range(n):
                    matrix[b][a] = 0
                    
# more efficient implementation to use the first row and col of the matrix as the lookup arrays and an extra variable for [0][0]
