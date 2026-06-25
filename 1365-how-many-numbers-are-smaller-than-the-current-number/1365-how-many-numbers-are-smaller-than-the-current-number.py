class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        temp = sorted(nums)
        first = {}

        for i, num in enumerate(temp):
            if num not in first:
                first[num] = i

        ans = []

        for num in nums:
            ans.append(first[num])

        return ans