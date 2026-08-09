class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack=[]

        for c in num:
            while k>0 and stack and stack[-1]>c:
                k-=1
                stack.pop()
            stack.append(c)
        
        stack=stack[:len(stack)-k]
        res="".join(stack)
        i = 0
        while i < len(res) and res[i] == "0":
            i += 1
        
        res = res[i:] if i < len(res) else "0"
        return res