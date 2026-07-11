class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        c1=0
        copy=n
        while copy:
            c1+=1
            copy=copy//10
        c2=0
        f=0
        while n:
            c2+=1
            r=n%10
            n=n//10
            if r==x:
                if c1!=c2:
                    f=1
                else:
                    f=0
        return f==1