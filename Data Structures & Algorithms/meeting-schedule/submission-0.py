"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        We should sort meetings by start time, so we know which meeting we have entered first.
        Given we are in a meeting, at what time will it end?
        -- will it conflict with any of the upcoming meetings' start times?
        intervals = [(0,30),(5,10),(15,20)]
        |---------------------------|
                |-----|
                           |-----|
        """
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            prev_interval = intervals[i-1]
            curr_interval = intervals[i]

            if curr_interval.start < prev_interval.end:
                return False
        
        return True