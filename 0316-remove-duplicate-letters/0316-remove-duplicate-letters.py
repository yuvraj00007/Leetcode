class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        seen=set()
        last={}

        for i,ch in enumerate(s):
            last[ch]=i
        
        for i , ch in enumerate(s):
            if ch in seen:
                continue


            while stack and stack[-1]>ch and last[stack[-1]]>i:
                seen.remove(stack.pop())

            seen.add(ch)
            stack.append(ch)
        
        return "".join(stack)