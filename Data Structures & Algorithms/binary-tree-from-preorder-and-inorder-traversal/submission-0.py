# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indicies = {}
        for i in range(len(inorder)):
            inorder_indicies[inorder[i]] = i
        
        self.preorder_index = 0
        def dfs(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.preorder_index]
            self.preorder_index += 1

            root = TreeNode(root_val)

            mid = inorder_indicies[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)