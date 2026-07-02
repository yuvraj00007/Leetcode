class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        se=0
        so=0
        if n%2!=0:
            so=so+n
        else:
            se=se+n
        return gcd(se,so)
    
        