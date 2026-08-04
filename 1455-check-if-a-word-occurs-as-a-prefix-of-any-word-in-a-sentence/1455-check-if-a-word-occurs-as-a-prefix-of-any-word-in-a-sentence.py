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

            if len(s) >= len(searchWord):
                match = True
                for j in range(len(searchWord)):
                    if s[j] != searchWord[j]:
                        match = False
                        break

                if match:
                    return index

        return -1