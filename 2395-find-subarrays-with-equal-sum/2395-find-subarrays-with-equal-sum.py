class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        window=sum(nums[:2])
        ans=set()
        ans.add(window)
        for i in range(2,len(nums)):
            window+=nums[i]
            window-=nums[i-2]
            if window in ans:
                return True
            ans.add(window)
        return False