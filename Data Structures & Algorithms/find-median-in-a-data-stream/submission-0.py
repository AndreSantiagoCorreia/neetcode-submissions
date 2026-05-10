class MedianFinder:

    def __init__(self):
        """
        In this problem, we can add any number at any time, we will need to keep it sorted so it's easy to find a median
        Leverage one min and one max heap
        
        max / min
        - / 1
        - / 1,3 -> need to rebalance 1 / 3
        1,2 / 3
        1,2 / 3,4
        1,2,2 / 3,4
        1,2,2,2 / 3,4 -> need to rebalance 1,2,2 / 2,3,4
        """
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
        # add value to min_heap (right side of sorted array), if it's greater than or equal to it's minimum value
        elif self.min_heap[0] <= num:
            # before adding to min_heap, check if we will need a rebalance, if so, pop and add to max_heap
            if len(self.min_heap) == len(self.max_heap) + 1:
                val = -heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, val)
            heapq.heappush(self.min_heap, num)
        # otherwise, add to max_heap (left side of sorted array)
        else:
            # before adding to max_heap, check if we will need a rebalance, if so, pop and add to min_heap
            if len(self.max_heap) == len(self.min_heap) + 1:
                val = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, val)
            heapq.heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        # this will only be called after adding at least one integer to the data structure, no need to check.
        # even-case, need to peek both and average result
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return self.min_heap[0] if len(self.min_heap) > len(self.max_heap) else -self.max_heap[0]
        