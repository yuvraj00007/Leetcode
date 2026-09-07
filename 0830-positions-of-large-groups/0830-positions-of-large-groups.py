class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        start = 0

        for i in range(1, len(s) + 1):

            if i == len(s) or s[i] != s[i - 1]:

                length = i - start

                if length >= 3:
                    ans.append([start, i - 1])

                start = i

        return ans