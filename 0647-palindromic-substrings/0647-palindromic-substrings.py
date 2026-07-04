class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0

        for i in range(len(s)):

            l=r=i
            while l>=0 and r<len(s):
                if s[l]==s[r]:
                    ans+=1
                    l-=1
                    r+=1
                else:
                    break


        for i in range(len(s)):
            l=i
            if len(s)>1:
                r=i+1
            while l>=0 and r<len(s):
                if s[l]==s[r]:
                    ans+=1
                    l-=1
                    r+=1
                else:
                    break

        return ans