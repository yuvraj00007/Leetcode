class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and not (
                ('a' <= s[l] <= 'z') or
                ('A' <= s[l] <= 'Z') or
                ('0' <= s[l] <= '9')
            ):
                l += 1

            while l < r and not (
                ('a' <= s[r] <= 'z') or
                ('A' <= s[r] <= 'Z') or
                ('0' <= s[r] <= '9')
            ):
                r -= 1

            c1 = s[l]
            c2 = s[r]

            if 'A' <= c1 <= 'Z':
                c1 = chr(ord(c1) + 32)

            if 'A' <= c2 <= 'Z':
                c2 = chr(ord(c2) + 32)

            if c1 != c2:
                return False

            l += 1
            r -= 1

        return True