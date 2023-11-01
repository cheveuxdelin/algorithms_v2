class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        preceding = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"],
        }

        total = 0

        for i in range(len(s)):
            if s[i] in preceding and i+1 < len(s) and s[i+1] in preceding[s[i]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        
        return total


