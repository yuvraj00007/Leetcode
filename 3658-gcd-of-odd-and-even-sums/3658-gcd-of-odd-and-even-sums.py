class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        even=0
        odd=0
        for i in range(1,n*2+1):
            if i%2==0:
                even+=i
            else:
                odd+=i
        return gcd(even,odd)
        
