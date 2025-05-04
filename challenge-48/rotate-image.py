class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        top = 0
        bottom = n-1

        # vertical revers
        while top < bottom:
            for col in range(n):
                matrix[top][col], matrix[bottom][col] = matrix[bottom][col], matrix[top][col]
            top += 1
            bottom -= 1

        # transpose  
        for row in range(n):
            for col in range(row+1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

# TC : O(N^2)
# SC : O(1)