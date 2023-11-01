class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        d = {}
        longest = 0
        for num in arr:
            d[num] = d.get(num-difference, 0) + 1
            longest = max(d[num], longest)
        return longest
