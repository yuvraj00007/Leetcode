class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        ans=[]
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                ans.append(nums[i])
                break

        for i in range(1,n+1):
            if i not in nums:
                ans.append(i)
        return ans