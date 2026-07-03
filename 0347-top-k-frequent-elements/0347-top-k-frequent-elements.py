from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}

        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        ans=[]
        
        arr=sorted(freq.items() ,key=lambda x:x[1],reverse=True)

        for i in range(k):
            ans.append(arr[i][0])
        
        return ans

