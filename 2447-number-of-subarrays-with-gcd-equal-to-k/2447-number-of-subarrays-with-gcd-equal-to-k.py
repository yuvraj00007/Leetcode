from typing import List

class Solution:
    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans=0
        
        for i in range(len(nums)):
            g=nums[i]
            if g<k:
                continue
            if g==k:
                ans+=1

            for j in range(i+1,len(nums)):
                if nums[j]<k:
                    break
                g=self.gcd(g,nums[j])

                if g==k:
                    ans+=1
                if g<k:
                    break
        return ans
