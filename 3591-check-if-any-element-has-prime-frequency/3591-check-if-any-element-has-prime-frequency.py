class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        
        h={}
        for num in nums:
            if num in h:
                h[num]+=1
            else:
                h[num]=1
        
        for n in h:
            x=h[n]
            c=0
            for i in range(1,x+1):
                if x%i==0:
                    c+=1
            if c==2:
                return True
        return False
