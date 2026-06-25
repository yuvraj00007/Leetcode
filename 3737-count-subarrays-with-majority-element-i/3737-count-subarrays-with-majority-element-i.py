class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        arr = []
        ans = 0
        for num in nums:
            if num == target:
                arr.append(1)
            else:
                arr.append(-1)

        for i in range(n):
            s = 0
            for j in range(i, n):
                s += arr[j]
                if s > 0:
                    ans += 1

        return ans