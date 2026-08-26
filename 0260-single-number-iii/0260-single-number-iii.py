class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0

        for num in nums:
            xor^=num
        
        mask= xor & -xor

        g1=0
        g2=0

        for num in nums:
            if num & mask:
                g1^=num
            else:
                g2^=num
        
        return [g1,g2]