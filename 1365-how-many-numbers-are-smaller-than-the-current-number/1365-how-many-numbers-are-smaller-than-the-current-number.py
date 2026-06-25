class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    
        arr=[]
        for i in range(len(nums)):
            ans=0
            if i!=0:
                for j in range(i):
                    if nums[j]<nums[i]:
                        ans+=1
            if i!=len(nums)-1:
                for k in range(i+1,len(nums)):
                    if nums[k]<nums[i]:
                        ans+=1
            arr.append(ans)
        return arr