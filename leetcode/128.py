class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        _max = 0
        for num in s:
            if num-1 not in s:
                i = num
                while i in s:
                    i += 1
                _max = max(_max, i-num)
        return _max
                