class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        
        maxHeap=[]

        for stone in stones:
            heapq.heappush(maxHeap,-stone)

        while maxHeap:
            a=-heapq.heappop(maxHeap)
            if maxHeap:
                b=-heapq.heappop(maxHeap)
            else:
                heapq.heappush(maxHeap,a)
                return maxHeap[0]
            

            if a==b:
                continue
            else:
                heapq.heappush(maxHeap,b-a)
            
        return 0

