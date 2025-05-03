class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        c, r, dc, dr = 0, 0, 1, 0

        for _ in range(rows * cols):
            res.append(matrix[r][c])
            matrix[r][c] = "."

            if not 0 <= c + dc < cols or not 0 <= r + dr < rows or matrix[r+dr][c+dc] == ".":
                dc, dr = -dr, dc
            
            c += dc
            r += dr
        
        return res

# TC : O(M * N)
# SC O(1)