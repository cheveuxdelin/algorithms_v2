def longest_common_substring(s1: str, s2: str) -> int:
    def ƒ(i1: int, i2: int, c: int) -> int:
        if i1 == len(s1) or i2 == len(s2):
            return c

        if s1[i1] == s2[i2]:
            c = ƒ(i1+1, i2+2, c+1)

        return max(
            c,
            ƒ(i1, i2+1, 0),
            ƒ(i1+1, i2, 0),
        )

    return ƒ(0, 0, 0)


# TOP DOWN
def longest_common_substring(s1: str, s2: str) -> int:
    memo = {}

    def ƒ(i1: int, i2: int, count: int) -> int:
        if i1 >= len(s1) or i2 >= len(s2):
            return count

        if (i1, i2, count) in memo:
            return memo[(i1, i2, count)]

        c = count

        if s1[i1] == s2[i2]:
            c = ƒ(i1+1, i2+1, count+1)

        memo[(i1, i2, count)] = max(
            c,
            ƒ(i1+1, i2+1, 0),
            ƒ(i1, i2+1, 0)
        )

        return memo[(i1, i2, count)]

    return ƒ(0, 0, 0)


# BOTTOM UP
def longest_common_substring(s1: str, s2: str) -> int:
    n = len(s1)
    m = len(s2)

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    rtn = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                rtn = max(rtn, dp[i][j])
    return rtn


# BOTTOM UP SPACE OPTIMIZED
def longest_common_substring(s1: str, s2: str) -> int:
    dp = [0 for _ in range(len(s2)+1)]
    max_length = 0
    for i1 in range(1, len(s1)+1):
        for i2 in range(len(s2), 0, -1):
            if s1[i1-1] == s2[i2-1]:
                dp[i2] = 1 + dp[i2-1]
            else:
                dp[i2] = 0
            max_length = max(max_length, dp[i2])
    return max_length

x = longest_common_substring("educative", "education")