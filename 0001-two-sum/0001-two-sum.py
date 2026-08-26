class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        i=0
        for num in nums:
            if target-num in hm:
                return [hm[target-num],i]
            else:
                hm[num]=i
            i+=1