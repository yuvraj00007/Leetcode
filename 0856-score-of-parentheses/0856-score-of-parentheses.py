class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        i = 0

        while i < len(s):
            if s[i] == '(':
                stack.append(0)
            else:
                val = stack.pop()

                if val == 0:
                    val = 1
                else:
                    val = 2 * val

                stack[-1] += val

            i += 1

        return stack[0]