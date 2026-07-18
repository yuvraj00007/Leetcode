class Solution:
    def countPoints(self, rings: str) -> int:
        n=len(rings)
        hm={}
        for i in range(0,len(rings),2):
            color=rings[i]
            rod=rings[i+1]

            if rod not in hm:
                hm[rod]=set()
            
            hm[rod].add(color)

        ans=0
        for colors in hm.values():
             if len(colors)==3:
                ans+=1
        return ans
        
            