class Solution:
    def reverseDegree(self, s: str) -> int:
        m=1
        ans=0
        for i in range(len(s)):
            v=ord('z')-ord(s[i])+1
            ans+=v*m
            m+=1
        return ans