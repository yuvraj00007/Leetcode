class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[:4])

        months = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            months[1] = 29

        m = int(date[5:7])
        d = int(date[8:10])

        days = 0

        for i in range(m - 1):
            days += months[i]

        days += d

        return days