class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r, c):
            q = deque()
            q.append((r,c))
            grid[r][c] = '0'

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if ((0<= r < rows) and 
                        (0 <= c < cols) and 
                        grid[r][c] == '1' and 
                        (r,c)):
                        q.append((r,c))
                        grid[r][c] = '0'

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c):
                    bfs(r,c)
                    islands += 1
                    

        return islands

# TC : O(Rows∗Cols)
# SC : O(Rows∗Cols)