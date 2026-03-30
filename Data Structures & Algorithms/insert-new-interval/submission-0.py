class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        NOTE: intervals is initially sorted in ascending order by start_i.
        Goal: Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also 
            intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

        We can mantain a result array and append each interval, if one of our insertion condition hits, we return
        """
        res = []
        new_start, new_end = newInterval

        for i in range(len(intervals)):
            start, end = intervals[i]

            if end < new_start:
                # completely before
                res.append([start, end])

            elif start > new_end:
                # completely after → insert and finish
                res.append([new_start, new_end])
                return res + intervals[i:]

            else:
                # overlap → merge
                new_start = min(new_start, start)
                new_end = max(new_end, end)

        # if we never inserted it
        res.append([new_start, new_end])
        return res