# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        for each node, perform dfs to the left and to the right, compare both results
        - if they differ by 2 or more, return -1 and check that signal to return early.
        """
        def dfs(root):
            if not root:
                return 0
            
            lh = dfs(root.left)
            if lh == -1:
                return -1
            
            rh = dfs(root.right)
            if rh == -1:
                return -1
            
            if abs(lh - rh) > 1:
                return -1
            
            return max(lh, rh) + 1
        
        return dfs(root) != -1