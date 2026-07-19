class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()

        hm = {}
        s = ""

        for ch in paragraph:
            if ch.isalpha():
                s += ch
            else:
                if s:
                    hm[s] = hm.get(s, 0) + 1
                    s = ""

        #forrr last word
        if s:
            hm[s] = hm.get(s, 0) + 1

        ans = ""
        mx = 0

        for word in hm:
            if word not in banned and hm[word] > mx:
                mx = hm[word]
                ans = word

        return ans