class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)



        prefixGcd=[]
        mx=nums[0]
        for i in range(len(nums)):
            mx=max(mx,nums[i])
            prefixGcd.append(gcd(nums[i],mx))
        
        prefixGcd.sort()

        l=0
        r=len(prefixGcd)-1
        summ=0
        while l<r:
            summ+=gcd(prefixGcd[l],prefixGcd[r])
            l+=1
            r-=1
        return summ
