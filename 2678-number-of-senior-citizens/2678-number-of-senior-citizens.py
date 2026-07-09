class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans=0
        for d in details:
            f=int(d[11])
            s=int(d[12])
            num=10*f+s
            if num>60:
                ans+=1
            
        return ans
