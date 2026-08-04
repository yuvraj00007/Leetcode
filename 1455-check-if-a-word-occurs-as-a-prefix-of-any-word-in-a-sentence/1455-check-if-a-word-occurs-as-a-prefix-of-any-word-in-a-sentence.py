class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str):

        i = 0
        s = ""
        index = 1

        while i < len(sentence):
            if sentence[i] == " ":
                s = ""
                index += 1
                i += 1
                continue

            s += sentence[i]
            i += 1

            if s.startswith(searchWord):
                return index

        return -1