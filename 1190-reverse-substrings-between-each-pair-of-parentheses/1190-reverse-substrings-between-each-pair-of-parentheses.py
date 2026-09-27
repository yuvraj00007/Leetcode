class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                stack.append("")
            elif s[i] == ')':
                temp = stack.pop()
                temp = temp[::-1]

                if stack:
                    stack[-1] += temp
                else:
                    stack.append(temp)
            else:
                if stack:
                    stack[-1] += s[i]
                else:
                    stack.append(s[i])

            i += 1

        return stack[0]