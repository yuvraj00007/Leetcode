class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)

        ans = 0
        c = 0

        for i in count:
            if count[i] % 2 != 0 and c == 0:
                ans += count[i]
                c = 1
            elif count[i] % 2 != 0 and c == 1:
                ans += count[i] - 1
            else:
                ans += count[i]

        return ans