class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        N = len(word)

        def dfs(row, col, dept):
            if dept == N:
                return True
            
            if row >= rows or row < 0 \
            or col >= cols or col < 0 \
            or board[row][col] != word[dept]:
                return False
            
            temp = board[row][col]
            board[row][col] = "#"

            res = (dfs(row+1, col, dept+1) or
            dfs(row-1, col, dept+1) or
            dfs(row, col+1, dept+1) or
            dfs(row, col-1, dept+1))
            board[row][col] = temp

            return res
            


        for r in range(rows):
            for c in range(cols):
                if word[0] == board[r][c]:
                    if dfs(r,c, 0):
                        return True
                    
        return False


# TC : O(Row * Col * 3^L)
# SC : O(L)
# where L is the length of word