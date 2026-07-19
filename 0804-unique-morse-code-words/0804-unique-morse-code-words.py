class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans=set()
        for word in words:
            tmp=""
            for w in word:
                i=ord(w)-ord("a")
                tmp+=code[i]
            ans.add(tmp)
        return len(ans)
