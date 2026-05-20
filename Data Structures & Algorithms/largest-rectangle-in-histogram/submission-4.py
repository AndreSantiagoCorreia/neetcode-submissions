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
        stack = [] # Stores indices instead of heights
        res = 0

        # We use enumerate to have access to the current index 'i'
        for i, h in enumerate(heights):
            # Compare current height h with the height of the index at the top of the stack
            while stack and heights[stack[-1]] > h:
                pop_index = stack.pop()
                # If stack is empty, the popped bar was the shortest seen so far (spans from 0 to i)
                # Otherwise, it spans from the element after the new top of the stack up to i
                width = i if not stack else i - stack[-1] - 1
                curr_area = width * heights[pop_index]
                res = max(res, curr_area)
            
            stack.append(i) # Store the index
        
        # Process the remaining indices left in the stack
        # These bars can all extend to the very right end of the histogram (index len(heights))
        while stack:
            pop_index = stack.pop()
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            curr_area = width * heights[pop_index]
            res = max(res, curr_area)

        return res