class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            [1000, "M"],
            [500, "D"],
            [100, "C"],
            [50, "L"],
            [10, "X"],
            [5, "V"],
            [1, "I"]
        ]

        rtn = ""
        i = 0

        letter = 1
        value = 0

        while num:
            if num - values[i][value] >= 0:
                num -= values[i][value]
                rtn += values[i][letter]
            else:
                idx2 = i + 2 - i % 2
                if idx2 < len(values) and num - values[i][value] + values[idx2][value] >= 0:
                    num = num - values[i][value] + values[idx2][value]
                    rtn += values[idx2][letter] + values[i][letter]
                i += 1

        return rtn