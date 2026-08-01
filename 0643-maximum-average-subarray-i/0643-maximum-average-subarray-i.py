class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l,r=0,k-1
        summ=sum(nums[:k])
        avg=summ/k

        while r<len(nums)-1:
        
            summ-=nums[l]
            l+=1
            r+=1
            summ+=nums[r]
            avg=max(avg,summ/k)
        
        return avg
            
             