class Solution:
    def countCommas(self, n: int) -> int:
        t=n
        c=0
        while t:
            c+=1
            t=t//10
        
        if c<4:
            return 0
        
        return n-999