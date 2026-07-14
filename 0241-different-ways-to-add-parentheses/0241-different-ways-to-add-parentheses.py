class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans=[]

        for i in range(len(expression)):

            if expression[i] in "*+-":

                left=self.diffWaysToCompute(expression[:i])
                right=self.diffWaysToCompute(expression[i+1:])

                for l in  left :
                    for r in right:

                        if expression[i]=="*":
                            ans.append(l*r)
                        if expression[i]=="+":
                            ans.append(l+r)
                        if expression[i]=="-":
                            ans.append(l-r)
        if not ans:
            ans.append(int(expression))
        
        return ans