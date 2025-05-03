class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        column = len(matrix[0])
        
        first_row_zero = False
        first_col_zero = False

        # check if the first column contains zero
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True
                break

        # check if the first row contains zero
        for c in range(column):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        # set first column and row as zero
        for row in range(1, rows):
            for col in range(1, column):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in range(1, rows):
            if matrix[row][0] == 0:
                for col in range(1, column):
                    matrix[row][col] = 0

        for col in range(1, column):
            if matrix[0][col] == 0:
                for row in range(1, rows):
                    matrix[row][col] = 0
        
        if first_row_zero:
            for c in range(column):
                matrix[0][c] = 0
        
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0

# TC : O(M * N)
# SC : O(1)