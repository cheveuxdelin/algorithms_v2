class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-stone for stone in stones]
        heapq.heapify(h)

        while len(h) > 1:
            r1 = heapq.heappop(h)
            r2 = heapq.heappop(h)

            if r1 != r2:
                heapq.heappush(h, r1 - r2)
        
        return -h[0] if h else 0