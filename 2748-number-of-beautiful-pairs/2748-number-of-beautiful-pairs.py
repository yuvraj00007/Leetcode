class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        ans=0
        for i in range(len(nums)-1):
            t=nums[i]
            while t>9:
                t=t//10
            f=t
            
            for j in range(i+1,len(nums)):
                s=nums[j]%10
                x=gcd(f,s)
                if x==1:
                    ans+=1
        return ans