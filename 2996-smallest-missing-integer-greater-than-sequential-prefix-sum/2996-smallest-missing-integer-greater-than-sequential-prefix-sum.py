class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seq = nums[0]
        s = nums[0]

        if len(nums) == 1:
            return nums[0] + 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                s += nums[i]
                seq = s
            else:
                break

        while 1:
            if seq not in nums:
                return seq
            else:
                seq += 1