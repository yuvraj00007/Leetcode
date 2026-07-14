class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])

        memo={}
        def solve(i,j):

            if i>=n or j>=m:
                return float('inf')
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i==n-1 and j==m-1:
                return grid[i][j]
            
            memo[(i,j)]= grid[i][j] + min(
                solve(i+1,j),
                solve(i,j+1)
            )
            return memo[(i,j)]
        return solve(0,0)