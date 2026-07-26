class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        m=0
        self.islands=0
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
                return
            
            grid[r][c]=0
            self.islands+=1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    dfs(r,c)
                    m=max(self.islands,m)
                    self.islands=0
        return m

