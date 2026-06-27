class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=0
        for a in accounts:
            summ=0
            for b in a:
                summ+=b
            ans=max(ans,summ)
        return ans