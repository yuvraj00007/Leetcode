class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minimum=min(nums)
        maximum=max(nums)

        while minimum:
            temp=minimum
            minimum=maximum % minimum
            maximum=temp
        return maximum
