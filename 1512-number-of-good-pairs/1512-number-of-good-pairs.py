class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=0
        for c in count.values():
            ans += (c * (c - 1)) // 2
        return ans
