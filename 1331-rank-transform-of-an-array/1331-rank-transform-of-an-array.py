class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        rank={}

        unique=sorted(set(arr))

        r=1
        for num in unique:
            rank[num]=r
            r+=1
        
        ans=[]

        for num in arr:
            ans.append(rank[num])
        return ans