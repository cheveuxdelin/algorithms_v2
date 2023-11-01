class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0 for _ in range(len(text2)+1)]
        for i in range(len(text1)):
                for j in range(1, len(text2)+1):
                    if text1[i] == text2[j-1]:
                        dp[j] = 1 + dp[j-1]
                    else:
                        dp[j] = max(dp[j], dp[j-1])
        return dp[-1]