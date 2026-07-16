class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        res = ""
        pnum = abs(num)

        while pnum > 0:
            r = pnum % 7
            pnum //= 7

            res = str(r) + res   # prepend instead of appending

        if num < 0:
            return "-" + res
        else:
            return res