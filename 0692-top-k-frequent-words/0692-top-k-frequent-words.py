class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap=[]
        count=Counter(words)
        for word , freq in count.items():
            heapq.heappush(heap,(-freq,word))

        ans=[]

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans