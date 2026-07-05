class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid = nums[len(nums) // 2]
        cnt = 0

        for num in nums:
            if num == mid:
                cnt += 1

        return cnt == 1