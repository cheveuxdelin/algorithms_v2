class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        def fast_sum(n: int) -> int:
            return n*(n+1)//2
        c = 1
        rtn = 0
        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                c += 1
            else:
                rtn += fast_sum(c)
                c = 1
        rtn += fast_sum(c)
        return rtn

        