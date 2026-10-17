class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(num):
            summ = 0
            while num:
                summ += num % 10
                num //= 10
            return summ

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {num: i for i, num in enumerate(nums)}
        ans = 0

        for i, num in enumerate(arr):
            if nums[i] != num:
                j = pos[num]
                nums[i], nums[j] = nums[j], nums[i]
                pos[nums[j]] = j
                pos[nums[i]] = i
                ans += 1

        return ans