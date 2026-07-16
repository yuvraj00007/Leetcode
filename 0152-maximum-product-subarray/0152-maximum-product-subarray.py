class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        cmax,cmin=1,1
        res=max(nums)
        for num in nums:
            if num==0:
                cmax,cmin=1,1
                continue
            
            tmp=cmax

            cmax=max(cmax*num , cmin*num,num)
            cmin=min(tmp*num , cmin*num,num)

            res=max(res,cmax)
        
        return res