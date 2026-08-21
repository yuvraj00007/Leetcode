class Solution:
    def countAndSay(self, n: int) -> str:
        s1 = "1"

        for _ in range(n - 1):
            s2 = ""
            i = 0

            while i < len(s1):
                c = 1

                while i + 1 < len(s1) and s1[i] == s1[i + 1]:
                    c += 1
                    i += 1

                s2 += str(c)
                s2 += s1[i]

                i += 1

            s1 = s2

        return s1