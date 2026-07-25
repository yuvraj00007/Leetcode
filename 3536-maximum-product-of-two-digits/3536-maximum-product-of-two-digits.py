class Solution:
    def maxProduct(self, n: int) -> int:
        m=0
        arr=[]

        while n:
            arr.append(n%10)
            n=n//10
        
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                m=max(m,arr[i]*arr[j])
        return m