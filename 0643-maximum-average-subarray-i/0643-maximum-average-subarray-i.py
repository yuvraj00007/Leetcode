class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=sum(nums[:k])
        ans=window

        for i in range(k,len(nums)):
            window+=nums[i]
            window-=nums[i-k]
            ans=max(ans,window)

        return ans/k