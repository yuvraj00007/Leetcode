class Solution:
    def maxDepth(self, s: str) -> int:
        i=0
        ans=0
        m=0
        while i<len(s):
            if s[i]=="(":
                ans+=1
            elif s[i]==")":
                ans-=1
            m=max(m,ans)
            i+=1
        return m