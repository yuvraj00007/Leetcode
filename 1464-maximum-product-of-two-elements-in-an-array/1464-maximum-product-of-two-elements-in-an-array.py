class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        f=nums[0]
        s=nums[1]

        return (f-1)*(s-1)

