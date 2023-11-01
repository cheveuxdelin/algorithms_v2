class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        c = 0
        for i in spaces:
            s = s[:i+c] + " " + s[i+c:]
            c += 1
        return s