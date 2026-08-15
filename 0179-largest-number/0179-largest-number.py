class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=[str(x) for x in nums]

        def mergesort(arr):
            if len(arr)<=1:
                return arr

            mid=len(arr)//2
            left=mergesort(arr[:mid])
            right=mergesort(arr[mid:])

            return merge(left,right)


        def merge(left,right):
            res=[]
            i=0
            j=0
            while i<len(left) and j<len(right):
                if left[i] + right[j] > right[j] + left[i]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
                
            while i < len(left):
                res.append(left[i])
                i += 1

            while j < len(right):
                res.append(right[j])
                j += 1

            return res

        
        nums=mergesort(nums)
        
        
        if nums[0]=="0":
            return "0"
        
        return "".join(nums)