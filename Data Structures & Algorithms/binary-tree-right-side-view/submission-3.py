# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: DFS
        - TC = O(n), SC = O(n)
        - go all the way to the right and whenever there is a node
            and that node's height was not filled, that is the 
            right most node, then dfs to the left.
        """
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res

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