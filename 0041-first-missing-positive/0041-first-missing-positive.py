class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sett = set(nums)
        n = len(nums)

        for i in range(1, n + 2):
            if i not in sett:
                return i