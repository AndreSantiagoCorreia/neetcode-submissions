class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        For every two intervals we need to decide if:
        - first interval is completely independent (append it)
        - both overlap (merge them)
        """
        
        # sort intervals based on start time
        intervals.sort(key=lambda x: x[0])
        res = []        
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            # if current starts after, just append it
            if res[-1][1] < start:
                res.append([start, end])
            else:
                res[-1] = [min(start, res[-1][0]), max(end, res[-1][1])]

        return res