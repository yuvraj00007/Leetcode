class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def dfs(l,r,p1,p2,turn):
            if l>r:
                return p1>=p2
            if turn:
                return(
                    dfs(l+1,r,p1+nums[l],p2,False)
                    or
                    dfs(l,r-1,p1+nums[r],p2,False)
                )
            else:
                return(
                    dfs(l+1,r,p1,p2+nums[l],True)
                    and
                    dfs(l,r-1,p1,p2+nums[r],True)
                )



        return dfs(0,len(nums)-1,0,0,True)