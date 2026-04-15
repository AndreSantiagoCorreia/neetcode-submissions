class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones] # MAX HEAP
        heapq.heapify(heap)

        while len(heap) > 1:
            stone = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            smash = abs(stone - stone2)
            heapq.heappush(heap, -smash)
        
        return -heap[-1]
