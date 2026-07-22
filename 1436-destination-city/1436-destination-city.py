class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hm={}

        for a,b in paths:
            hm[a]=b
        
        for x in hm.values():
            if x not in hm:
                return x