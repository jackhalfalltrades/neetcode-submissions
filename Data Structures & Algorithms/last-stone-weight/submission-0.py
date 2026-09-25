from _heapq import heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        curr = [-x for x in stones]
        heapq.heapify(curr)

        while len(curr)> 1:
            x = heapq.heappop(curr)
            y = heapq.heappop(curr)

            if x != y:
                heapq.heappush(curr, x - y)

        return -curr[0] if curr else 0
