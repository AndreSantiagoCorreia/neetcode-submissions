# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS approach :) 
        """
        if not root:
            return []

        queue = deque()
        queue.append(root)
        results = []

        while queue:
            n = len(queue)
            level_nodes = []

            for i in range(n):
                curr_node = queue.popleft()
                level_nodes.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            
            results.append(level_nodes)

        return results