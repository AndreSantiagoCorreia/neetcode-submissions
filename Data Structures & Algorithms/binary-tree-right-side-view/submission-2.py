# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: BFS
        - TC = O(n), SC = O(n)
        - for each level, store to the resulting array only the
            last element from the queue 
        """
        queue = deque()
        if root:
            queue.append(root)
        res = []

        while queue:
            # iterate only over the elements of this current level
            n = len(queue)
            curr = None
            for _ in range(n):
                curr = queue.popleft()
                # always store from left to right
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            res.append(curr.val)

        return res