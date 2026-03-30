class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        For every two intervals if they overlap:
        - increase counter
        - keep smallest endTime to continue the sequence (as if we had removed the one that end later)
        """
        
        # sort intervals based on start time
        intervals.sort(key=lambda x: x[0])
        prev_start, prev_end = intervals[0]
        res = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            # if current starts after, just update new times
            if prev_end <= start:
                prev_start, prev_end = start, end
            # they conflict, update counter and resolve shortest interval
            else:
                res += 1
                prev_end = min(end, prev_end)

        return res