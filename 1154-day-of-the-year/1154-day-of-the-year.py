class Solution:
    def dayOfYear(self, date: str) -> int:
        year=date[:4]
        year=int(year)
        months = {
              1: 31,
              2: 28,
              3: 31,
              4: 30,
              5: 31,
              6: 30,
              7: 31,
              8: 31,
              9: 30,
              10: 31,
              11: 30,
              12: 31
                      }

        if (year%4==0 and year%100!=0) or ( year %400==0):
            months[2]=29

        m=date[5:7]
        m=int(m)

        days=0
        
        for i in range(1,m):
            days+=months[i]
        
        days+=int(date[8:10])

        return days

