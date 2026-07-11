class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:   
        h={}
        t=n
        while t:
            num=t%10
            if num in h:
                h[num]+=1
            else:
                h[num]=1
            t=t//10
        m=float('inf')
        ans=[]
        
        for digit, value in h.items():
            if value < m:
                m = value
                ans = [digit]
            elif value == m:
                ans.append(digit)
        if len(ans)==1:
            return ans[0]
        else:
            return min(ans)