class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        resulting_string = ""

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                resulting_string += word1[i]
            if i < len(word2):
                resulting_string += word2[i]
        return resulting_string
