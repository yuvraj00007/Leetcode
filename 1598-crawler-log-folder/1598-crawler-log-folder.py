class Solution:
    def minOperations(self, logs: List[str]) -> int:
        path=0

        for log in logs:
            if log[:2]==".." and path>0:
                path-=1
            elif log[-1]=="/" and log[0]!=".":
                path+=1
        return path