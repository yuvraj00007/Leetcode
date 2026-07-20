class Solution:
    def largestEven(self, s: str) -> str:
        

        for i in range(len(s)-1,-1,-1):
            if int(s[i])%2!=0:
                s=s[:i]
            else:
                return s
        return s
