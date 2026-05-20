class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Approach: Stack
        - TC = O(n), SC = O(n)
        7   1   7   2   2   4
        7  2x1  7   2   2   4   5
               3x1 4x1 5x1 6x1
                   2x2 3x2 4x2 5x2
                           2x4 3x4

        stack=[]
        store 7
        see 1, 7 > 1, pop 7, compute areas:
            width = 0
            while stack:
                width ++ 1
                area = width * stack.pop()
        see 7, stack[-1] <= 7, store 7.
        see 2, stack[-1] > 2, compute areas:
            idem...
        """
        stack = []
        # We need to track the widths corresponding to the heights in our stack
        # To keep a single stack of heights, we can pass the inherited width forward
        res = 0

        for h in heights:
            running_width = 0
            # Only pop elements that are strictly greater than the current height h
            while stack and stack[-1] > h:
                # Instead of width += 1, we need to know how wide the popped element was.
                # Since we only store heights, we must track the accumulated width 
                # of all strictly taller bars destroyed by 'h'.
                running_width += 1 
                curr_area = running_width * stack.pop()
                res = max(res, curr_area)
            
            # Key fix: If we popped taller elements, the current height 'h' 
            # can extend to the left into their territory.
            # We push 'h' multiple times to represent its total extended width.
            for _ in range(running_width + 1):
                stack.append(h)
        
        width = 0
        while stack:
            width += 1
            curr_area = width * stack.pop()
            res = max(res, curr_area)

        return res