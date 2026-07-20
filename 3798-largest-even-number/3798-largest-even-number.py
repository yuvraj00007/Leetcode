class Solution:
    def largestEven(self, s: str) -> str:
        

        i = len(s) - 1

        while i >= 0 and int(s[i])%2!=0:
            i -= 1

        return s[:i + 1]