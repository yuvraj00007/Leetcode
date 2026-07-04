class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        for i in range(len(s)):

            ans+=1
            for j in range(i+1,len(s)):
                l=i
                r=j
                sub=s[l:r+1]
                if sub==sub[::-1]:
                    ans+=1
        return ans
