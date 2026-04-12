# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        The root will always be a good node as it has no parent node.
        For the other nodes:
        -> dfs, while keeping track of curr_max from root.
            If the curr_node.val >= curr_max: we can increment the result
        """
        if not root:
            return 0

        self.good_nodes = 1 # root is good node already :)

        def dfs(node, curr_max):
            if not node:
                return
            
            if node.val >= curr_max:
                curr_max = node.val
                self.good_nodes += 1
            
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)

        dfs(root.left, root.val)
        dfs(root.right, root.val)
        return self.good_nodes