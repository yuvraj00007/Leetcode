class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        heapq.heapify(nums)

        while nums:
            a=heapq.heappop(nums)
            b=heapq.heappop(nums)

            arr.append(b)
            arr.append(a)
        
        return arr
            