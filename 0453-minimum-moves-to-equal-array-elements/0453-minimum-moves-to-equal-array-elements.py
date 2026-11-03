class Solution:
    def minMoves(self, nums: list[int]) -> int:
        ans=0
        m=min(nums)

        for num in nums:
            ans+=num-m
        return ans
            