class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for ch in s:
            if ord("0")<=ord(ch)<=ord("9"):
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)