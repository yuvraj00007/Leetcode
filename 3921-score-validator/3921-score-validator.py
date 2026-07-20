class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        s=0
        c=0
        for event in events:
            if c>9:
                break
            if event=="W":
                c+=1
            else:
                if event=="WD" or event=="NB":
                    s+=1
                else:
                    s+=int(event)
            
        return [s,c]