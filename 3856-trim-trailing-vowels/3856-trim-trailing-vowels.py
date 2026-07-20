class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        
        for i in range(len(s)-1,-1,-1):
            if s[i] in "aeiou":
                s=s[:i]
            else:
                break
        return s