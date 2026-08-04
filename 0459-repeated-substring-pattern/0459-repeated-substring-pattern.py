class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        n=len(s)

        for l in range(1,n//2 +1):

            if n%l!=0:
                continue

            sub=s[:l] 
            if sub*(n//len(sub))==s:
                return True
        return False