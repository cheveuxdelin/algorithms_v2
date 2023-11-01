class Solution:
    def partitionString(self, s: str) -> int:
        char_set = set()
        rtn = 1
        for i in range(len(s)):
            if s[i] in char_set:
                rtn += 1
                char_set = set()
            char_set.add(s[i])
        return rtn