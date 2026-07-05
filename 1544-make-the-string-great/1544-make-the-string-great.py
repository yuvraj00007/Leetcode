class Solution:
    def makeGood(self, s: str) -> str:
        
        i=1

        while i<len(s):
            if abs(ord(s[i])-ord(s[i-1]))==32:
                s=s[:i-1]+s[i+1:]
                i=1
            else:

                i+=1
        return s