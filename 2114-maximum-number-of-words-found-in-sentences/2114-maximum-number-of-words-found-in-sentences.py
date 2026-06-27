class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        for p in sentences:
            c=1
            for i in p:
                if not i.isalnum():
                    c+=1
            ans=max(ans,c)
        return ans