class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        d=n

        while 1:
            summ=1
            
            temp=d
            while temp:
                r=temp%10
                temp=temp//10
                summ*=r
            if summ%t==0:
                return d
            d+=1


