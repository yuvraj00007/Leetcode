class Solution:
    def sumAndMultiply(self, n: int) -> int:
        c=1
        num=0
        s=0
        while n:
            r=n%10
            
            if r:

                num=r*c+num
                s+=r
                c=c*10
            n=n//10
            
        return num*s