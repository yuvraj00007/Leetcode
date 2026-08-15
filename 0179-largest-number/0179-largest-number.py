class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                a=str(nums[i])
                b=str(nums[j])

                if a+b<b+a:
                    nums[i],nums[j]=nums[j],nums[i]
        ans=""
        for i in range(len(nums)):
            ans+=str(nums[i])
        
        if ans[0]=="0":
            return "0"
        return ans