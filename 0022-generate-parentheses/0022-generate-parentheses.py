class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def helper(lp,rp,s):
            if len(s)==n*2:
                ans.append(s)
                return
            if lp<n:
                helper(lp+1,rp,s+'(')
            if rp<lp:
                helper(lp,rp+1,s+')')
        
        helper(0,0,'')
        return ans