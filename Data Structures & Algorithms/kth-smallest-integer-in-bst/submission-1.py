# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        We need to go left until there is no more root.left
        - count ++
        We come back to the root
        - count ++
        We go right (if any)
        - count ++
        whenever count == k, return
        """
        self.count = 0
        self.result = None

        def dfs(root):
            if not root or self.result != None:
                return
            dfs(root.left)
            self.count += 1
            
            if self.count == k:
                self.result = root.val
                return
            
            dfs(root.right)
            
        dfs(root)
        return self.result