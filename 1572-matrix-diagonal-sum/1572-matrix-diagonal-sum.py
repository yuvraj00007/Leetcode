class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        i=0
        j=0
        s=0
        while i<n and j<n:
            s+=mat[i][j]
            i+=1
            j+=1
        
        i=n-1
        j=0
        while i>=0 and j<n:
            s+=mat[i][j]
            i-=1
            j+=1

        if n % 2 == 1:
            s -= mat[n // 2][n // 2]
        return s
        

