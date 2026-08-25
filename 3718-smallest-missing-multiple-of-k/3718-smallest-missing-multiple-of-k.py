class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums=set(nums)
        temp=k
        while 1:
            if temp in nums:
                temp+=k
            else:
                return temp
            
