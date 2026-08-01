class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        # Customers already satisfied
        base = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]

        window=0
        for i in range(minutes):
            window+=customers[i]*grumpy[i]
        ans=window

        for i in range(minutes,len(customers)):
            window+=(customers[i]*grumpy[i])
            window-=customers[i-minutes]*grumpy[i-minutes]
            ans=max(ans,window)
        return base+ans