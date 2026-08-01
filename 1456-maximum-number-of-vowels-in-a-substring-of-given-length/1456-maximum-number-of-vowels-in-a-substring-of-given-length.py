class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels="aeiou"

        ans=0

        window=s[:k]
        for w in window:
            if w in vowels:
                ans+=1
        m=ans
        
        for i in range(k,len(s)):
            if s[i-k] in vowels:
                ans-=1
            if s[i] in vowels:
                ans+=1
            m=max(m,ans)
        return m