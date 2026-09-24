class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        i=0
        for num in nums:

            s=0
            while num:
                rem=num%10
                num//=10
                s+=rem
            if s==i:
                return i
            i+=1
        return -1