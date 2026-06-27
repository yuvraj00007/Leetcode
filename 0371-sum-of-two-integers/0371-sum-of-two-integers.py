class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xFFFFFFFF
        maxInt=2**31-1
        while b:
            sums=(a^b)&mask
            carry=(a&b)&mask
            a,b=sums,carry<<1
        return a if a<=maxInt else ~(a^mask)
            