class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n=len(nums)
        m=n//2 
        if n==1:
            return True
        x=nums[m]
        nums.remove(x)
        s=set(nums)

        if x in s:
            return False
        
        return True
            