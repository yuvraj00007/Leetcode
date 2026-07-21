class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxHeap=[]

        for num in arr:
            heapq.heappush(maxHeap,(-abs(x-num),-num))

            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        ans=[]
        while maxHeap:
            d,num = heapq.heappop(maxHeap)
            ans.append(-num)
        ans.sort()
        return ans