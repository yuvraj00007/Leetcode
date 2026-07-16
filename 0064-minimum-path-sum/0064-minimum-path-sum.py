class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])

        dp=[[0]*m for _ in range(n+1)]

        dp[n-1][m-1]=grid[n-1][m-1]

        for i in range(m-2,-1,-1):
            dp[n-1][i]=grid[n-1][i]+dp[n-1][i+1]

        for j in range(n-2,-1,-1):
            dp[j][m-1]=grid[j][m-1]+dp[j+1][m-1]

        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                dp[i][j]=grid[i][j]+min(
                    dp[i+1][j],
                    dp[i][j+1]
                )
        return dp[0][0]