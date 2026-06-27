class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=""
        for l in address:

            if l==".":
                ans+="[.]"
            else:
                ans+=l
                
        return ans