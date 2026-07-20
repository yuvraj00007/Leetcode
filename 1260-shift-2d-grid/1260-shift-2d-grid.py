class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        arr = []

        for row in grid:
            arr.extend(row)
        
        k%=(n*m)

        arr=arr[-k:]+arr[:-k]

        idx=0
        ans=[]
        for i in range(n):
            ans.append(arr[idx:idx+m])
            idx+=m
        return ans