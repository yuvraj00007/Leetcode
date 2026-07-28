class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        rows=len(grid)
        cols=len(grid[0])

        def helper(r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return 0
            
            if grid[r][c]==0:
                return 0
            
            grid[r][c]=0
            return (1+
            helper(r+1,c)+
            helper(r,c+1)+
            helper(r-1,c)+
            helper(r,c-1)
            )

        for r in range(rows):
            if grid[r][0]==1:
                helper(r,0)
            if grid[r][cols-1]==1:
                helper(r,cols-1)

        for c in range(cols):
            if grid[0][c]==1:
                helper(0,c)
            if grid[rows-1][c]==1:
                helper(rows-1,c)
        
        ans=0

        for r in range(1,rows-1):
            for c in range(1,cols-1):
                if grid[r][c]==1:
                    ans+=helper(r,c)
        
        return ans
                

            