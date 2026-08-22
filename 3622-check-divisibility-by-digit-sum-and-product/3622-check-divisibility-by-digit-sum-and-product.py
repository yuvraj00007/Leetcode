class Solution:
    def checkDivisibility(self, n: int) -> bool:
        m=1
        s=0
        x=n
        temp=n
        while temp:
            r=temp%10
            s+=r
            temp=temp//10
        while n:
            r=n%10
            m*=r
            n=n//10
        
        return x%(s+m)==0