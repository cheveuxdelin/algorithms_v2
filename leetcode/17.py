class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]

        result = []

        def ƒ(p):
            if len(p) == len(digits):
                result.append(p)
            else:
                for letter in letters[int(digits[len(p)])]:
                    ƒ(p+letter)
        ƒ("")

        return result