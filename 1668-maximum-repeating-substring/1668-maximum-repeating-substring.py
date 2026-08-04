class Solution:
    def maxRepeating(self, sequence: str, word: str):

        ans = 0
        d = word

        while len(d) <= len(sequence):
            if d in sequence:
                ans += 1
            else:
                break

            d += word

        return ans