class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            t=i
            app=0
            while t:
                if t%2:
                    app+=1
                t//=2
            ans.append(app)
        return ans
            

