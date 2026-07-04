class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(l, r):

            st = ""

            while l >= 0 and r < len(s) and s[l] == s[r]:
                st = s[l:r+1]      # Update the current longest palindrome for this center
                l -= 1
                r += 1

            return st

        ans = ""

        for i in range(len(s)):

            s1 = expand(i, i)       # Odd length palindrome
            s2 = expand(i, i + 1)   # Even length palindrome

            if len(s1) > len(ans):
                ans = s1

            if len(s2) > len(ans):
                ans = s2

        return ans