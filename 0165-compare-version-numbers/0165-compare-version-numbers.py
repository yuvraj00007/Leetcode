class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = 0
        j = 0

        while i < len(version1) or j < len(version2):
            s1 = ""
            s2 = ""

            while i < len(version1) and version1[i] != ".":
                s1 += version1[i]
                i += 1

            if i < len(version1):
                i += 1

            while j < len(version2) and version2[j] != ".":
                s2 += version2[j]
                j += 1

            if j < len(version2):
                j += 1

            n1 = int(s1) if s1 else 0
            n2 = int(s2) if s2 else 0

            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1

        return 0