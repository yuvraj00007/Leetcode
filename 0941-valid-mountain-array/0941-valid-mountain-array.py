class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        dec=0
        only_inc=0
        only_dec=0
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                return False
            if arr[i]>arr[i-1]:
                if dec==1:
                    return False
                only_dec=1


            if arr[i]<arr[i-1]:
                dec=1
                only_inc=1
        if only_inc==0 or only_dec==0:
            return False
        return True