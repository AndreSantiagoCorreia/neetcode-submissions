class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        keep two pointers, one starting on left-end and another on right-end
        move the one with smaller height, keep maxRes
        """
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            curr_area = (r - l) * min(heights[r], heights[l]) 
            res = max(res, curr_area)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1

        return res