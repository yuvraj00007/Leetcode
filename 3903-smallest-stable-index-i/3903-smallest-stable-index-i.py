class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        

        for i in range(len(nums)):
            m=0
            if i==0:
                m=nums[i]
            for j in range(i):
                m=max(m,nums[j])
            mn=float('inf')
            for j in range(i,len(nums)):
                mn=min(mn,nums[j])
            if m-mn<=k:
                return i
        return -1