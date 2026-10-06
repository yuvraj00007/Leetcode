class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ans = 0
        
        for c in s:
            if c == '(':
                stack.append(c)
            else:  # ')'
                if stack:
                    stack.pop()
                else:
                    ans += 1   # need one '('
        
        return ans + len(stack)