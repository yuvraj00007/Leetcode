class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output=[]

        for start,end in intervals:
            if end<newInterval[0]:
                output.append([start,end])
            elif start>newInterval[1]:
                output.append(newInterval)
                newInterval=[start,end]
            else:
                newInterval[0]=min(newInterval[0],start)
                newInterval[1]=max(newInterval[1],end)
        output.append(newInterval)
        return output