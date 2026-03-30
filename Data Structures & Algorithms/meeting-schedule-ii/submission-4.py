"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        Here we need to evaluate the maximum number of concurrent meetings at a time, 
            this will determine how many rooms we need to accommodate all meetings
        
        Heap approach:
        -- Push interval's end times to a min heap to keep track if a meeting has ended.
        -- Once we iterate through a new interval, we can check if the earliest meeting has ended by then
            If so, pop it.
        
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        heap = []  # stores end times

        for interval in intervals:
            # if earliest meeting ended → reuse room
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)

            heapq.heappush(heap, interval.end)

        return len(heap)