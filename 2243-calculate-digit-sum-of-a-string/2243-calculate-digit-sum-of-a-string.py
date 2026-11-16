class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            n = len(s) // k
            last = 0
            new = ""

            for i in range(n + 1):
                summ = 0

                if i < n:
                    for j in range(last, last + k):
                        summ += int(s[j])
                    last += k
                else:
                    for j in range(last, len(s)):
                        summ += int(s[j])

                if i < n or len(s) % k != 0:
                    new += str(summ)

            s = new

        return s