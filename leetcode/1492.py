class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        x = 1
        nth = 1
        while nth != k:
            x += 1
            if n % x == 0:
                nth += 1
            if x > n:
                return -1
        return x
