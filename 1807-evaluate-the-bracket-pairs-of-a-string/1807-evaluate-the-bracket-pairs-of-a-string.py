class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dict={}

        for key , val in knowledge:
            dict[key]=val
        
        i=0
        ans=""
        while i<len(s):

            if s[i]=="(":
                j=i+1

                while s[j]!=")":
                    j+=1
                word=s[i+1:j]
                if word in dict:
                    ans+=dict[word]
                else:
                    ans += "?"

                i = j + 1

            else:
                ans += s[i]
                i += 1

        return ans