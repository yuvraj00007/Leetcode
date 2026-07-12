class Solution:
    def tribonacci(self, n: int) -> int:
        f=0
        s=1
        t=1

        c=n-2
        if n==0:return 0
        if n==1:return 1
        if n==2:return 1
        if n==3:return 2
        
        while c:
            summ=(f+s+t)
            f=s
            s=t
            t=summ
            c-=1
        return summ