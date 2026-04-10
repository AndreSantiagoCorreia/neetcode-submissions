# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
            1
        2       3
      4  5    6   7

            1
        3       2
      6  7    4   5
        """
        left, right = None, None
        if not root:
            return root
        if root.left:
            left = root.left
        if root.right:
            right = root.right
        
        root.left, root.right = right, left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root