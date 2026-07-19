class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans=[]
        for word in words:
            tmp=""
            for w in word:
                i=ord(w)-ord("a")
                tmp+=code[i]
            if tmp not in ans:
                ans.append(tmp)
        return len(ans)
