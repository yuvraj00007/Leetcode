class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        ans=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        
        odd.sort()
        even.sort(reverse=True)

        for i in range(len(nums)):
            if i%2==0:
                ans.append(even.pop())
            else:
                ans.append(odd.pop())
        return ans
