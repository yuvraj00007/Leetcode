class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x

        if target < 0:
            return -1

        if target == 0:
            return len(nums)

        l = 0
        r = 0
        curr = 0
        longest = -1

        while r < len(nums):
            curr += nums[r]

            while curr > target:
                curr -= nums[l]
                l += 1

            if curr == target:
                longest = max(longest, r - l + 1)

            r += 1

        if longest == -1:
            return -1

        return len(nums) - longest