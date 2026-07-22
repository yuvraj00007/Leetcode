class Solution:
    def average(self, salary: List[int]) -> float:
        t=0
        c=len(salary)-2
        mn=min(salary)
        mx=max(salary)

        for i in range(len(salary)):
            if salary[i]!=mn and salary[i]!=mx:
                t+=salary[i]
                
        return t/c