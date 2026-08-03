class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        dp=[0]*n
        def solve(i):
            ans = float("-inf")
            if i >= n:
                return 0
            if dp[i] is not 0:
                return dp[i]
            if i < n:
                ans = max(ans, stoneValue[i] - solve(i + 1))
            if i + 1 < n:
                ans = max(ans,
                          stoneValue[i] + stoneValue[i + 1] - solve(i + 2))
            if i + 2 < n:
                ans = max(ans,
                          stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - solve(i + 3))
            dp[i]=ans
            return dp[i]
        res=solve(0)
        if res>0:
            return 'Alice'
        elif res<0:
            return 'Bob'
        else:
            return 'Tie'