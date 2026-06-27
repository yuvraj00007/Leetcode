class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        x=0
        for i in range(len(arr)):
            if x==1:
                x=0
                continue
            if arr[i]==0:
                arr.insert(i+1,0)
                arr.pop()
                x=1
                
                
                

        