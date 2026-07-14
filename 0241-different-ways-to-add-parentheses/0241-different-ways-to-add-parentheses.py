class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo={}

        def solve(expression):

            if expression in memo:
                return memo[expression]
            ans=[]

            for i in range(len(expression)):

                if expression[i] in "*+-":

                    left=solve(expression[:i])
                    right=solve(expression[i+1:])

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

            memo[expression]=ans
        
            return ans
        return solve(expression)