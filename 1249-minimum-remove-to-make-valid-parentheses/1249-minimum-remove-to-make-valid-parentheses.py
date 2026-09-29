class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = set()

        i = 0

        while i < len(s):
            if s[i] == '(':
                stack.append(i)

            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    remove.add(i)

            i += 1

        # Any '(' left in stack is unmatched
        while stack:
            remove.add(stack.pop())

        ans = ""
        i = 0

        while i < len(s):
            if i not in remove:
                ans += s[i]
            i += 1

        return ans