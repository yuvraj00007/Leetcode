class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        new=[]
        new=distance[:]+distance[:]
        n=len(distance)

        d1,d2=0,0
        if start>destination:
            start,destination = destination , start

        for i in range(start,destination):
            d1+=distance[i]

        for i in range(destination,start+n):
            d2+=new[i]
        
        return min(d1,d2)
