class Solution:
    def average(self, salary: List[int]) -> float:
        t=c=0

        mn=min(salary)
        mx=max(salary)

        for i in range(len(salary)):
            if salary[i]!=mn and salary[i]!=mx:
                t+=salary[i]
                c+=1
        return t/c