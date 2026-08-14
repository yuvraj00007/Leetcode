class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hm = {}
        ans = 0
        i = 0

        for j in range(len(s)):
            w = s[j]

            if w not in hm:
                hm[w] = 1
            else:
                hm[w] += 1

            while hm[w] > 2:
                hm[s[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)

        return ans