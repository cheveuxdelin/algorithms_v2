from collections import Counter
import heapq


# O(n + klogD)
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [i[0] for i in Counter(nums).most_common(k)]


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        c = Counter(nums)
        return [x[1] for x in heapq.nlargest(k, c.items(), key=lambda x: x[0])]
