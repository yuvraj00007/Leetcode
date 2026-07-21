class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        ans=0
        while nums:
            x=heapq.heappop(nums)
            if x==0:
                continue
            ans+=1

            tmp=[]
            while nums:
                val=heapq.heappop(nums)
                if val!=0:
                    tmp.append(val-x)
            for val in tmp:
                heapq.heappush(nums,val)
            
        return ans
