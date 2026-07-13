class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        ans=[]
        for c in range(len(str(low)),len(str(high))+1):
            s=""
            for i in range(1,c+1):
                s+=str(i)

            
            while True:

                if low<= int(s)<=high:
                    ans.append(int(s))
                
                if s[-1]=="9":
                    break
                
                s=s[1:]+str(int(s[-1])+1)
        return ans