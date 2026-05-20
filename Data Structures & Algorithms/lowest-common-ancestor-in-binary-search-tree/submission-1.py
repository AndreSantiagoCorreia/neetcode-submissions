# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Approach: Iterate over the tree doing Binary Search
        - TC = O(h), SC = O(1)
        All node values are unique
        if p > q make p < q
        - p, q = q, p
        If p <= curr_node.val <= q
            return curr_node.val
        else if q < curr_node.val, move curr_node to .left
        else move curr_node to the .right
        """
        if not root:
            return root
        if p.val > q.val:
            p, q = q, p
        
        while root:
            if p.val <= root.val <= q.val:
                return root
            elif q.val < root.val:
                root = root.left
            else:
                root = root.right
        
        return root