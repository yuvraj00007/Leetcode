class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        rev=s[:k]
        rem=s[k:]
        b=""
        for i in range(len(rev)-1,-1,-1):
            b+=rev[i]
        return b+rem