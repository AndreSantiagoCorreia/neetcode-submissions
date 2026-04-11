class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        First we need to count the frequencies, simple array traversal.
        Then we could sort the map in respect to frequencies and return the kth element -> O(n*logn)
        Better approach:
        Using a min_heap we can insert each entry of our frequency map as they come:
        - Once heap reaches length == k and heap.peek().freq < curr_entry.freq we will pop it and add curr_entry
        This will help us achieve O(n*logk) <= O(n*logn)
        """
        min_heap = []
        frequencies = defaultdict(int)
        
        for num in nums:
            frequencies[num] += 1
        
        for n, f in frequencies.items():
            if len(min_heap) == k:
                top_freq = min_heap[0][0]
                if top_freq < f:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (f, n))
            else:
                heapq.heappush(min_heap, (f, n))
        
        res = [entry[1] for entry in min_heap]
        return res
