class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        ans = ""

        while num1 or num2:
            n1 = int(num1[-1]) if num1 else 0
            n2 = int(num2[-1]) if num2 else 0

            temp = n1 + n2 + carry

            if temp > 9:
                carry = 1
            else:
                carry = 0

            ans += str(temp % 10)

            if num1:
                num1 = num1[:-1]
            if num2:
                num2 = num2[:-1]
        if carry:
            ans += "1"

        return ans[::-1]