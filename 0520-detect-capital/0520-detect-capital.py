class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        u=0
        l=0
        for w in word:
            if ord("a")<=ord(w)<=ord("z"):
                l+=1
            elif ord("A")<=ord(w)<=ord("Z"):
                u+=1
        if u==len(word) or l==len(word) or len(word)==1:
            return True
        if ord("A")<=ord(word[0])<=ord("Z") and l==len(word)-1:
            return True
        return False
