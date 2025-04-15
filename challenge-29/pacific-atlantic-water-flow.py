class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        R=len(grid)
        C=len(grid[0])
        res=[]
        pacific=[]
        atlantic=[]

        #right and left side
        for r in range(R):
            pacific.append((r,0,grid[r][0]))
            atlantic.append((r,C-1,grid[r][C-1]))
        #north and south side
        for c in range(C):
            pacific.append((0,c,grid[0][c]))
            atlantic.append((R-1,c,grid[R-1][c]))

        #pacific bfs
        pacific_reach=set()
        while pacific:
            r, c, h = pacific.pop()
            if (r, c) in pacific_reach:
                continue
            pacific_reach.add((r, c))
            nei = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for nr, nc in nei:
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] >= h:
                    pacific.append((nr, nc, grid[nr][nc]))
        

        #atlantic bfs
        atlantic_reach=set()
        while atlantic:
            r, c, h = atlantic.pop()
            if (r, c) in atlantic_reach:
                continue
            atlantic_reach.add((r, c))
            nei = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for nr, nc in nei:
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] >= h:
                    atlantic.append((nr, nc, grid[nr][nc]))
        for r,c in pacific_reach:
            if (r,c) in atlantic_reach:
                res.append((r,c))
        return res
    
# TC : O(R * C)
# SC : O(R * C)