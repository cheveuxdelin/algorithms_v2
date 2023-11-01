class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        rtn = []

        def ƒ(left, right, p):
            if len(p) == n*2:
                rtn.append(p)
            else:
                if left < n:
                    ƒ(left+1, right, p + "(")
                if left > right:
                    ƒ(left, right+1, p+")")

        ƒ(0, 0, "")
        return rtn
