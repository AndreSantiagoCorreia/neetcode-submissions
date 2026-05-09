# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        We will navigate the tree's left and right and they both need to return "True" as valid BST
        - Once we reach a leaf node, return true
        - If a node has at least one children, dfs into it, then validate the values 
           (left is less than root, right is greater than root)
        """
        def dfs(node, min_val, max_val):
            # Base: nó vazio é uma BST válida
            if not node:
                return True
                
            # O valor atual deve estar estritamente entre min_val e max_val
            if not (min_val < node.val < max_val):
                return False
                
            # Esquerda: atualiza o limite máximo com o valor do nó atual
            # Direita: atualiza o limite mínimo com o valor do nó atual
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        # Inicializa com infinito negativo e positivo
        return dfs(root, float('-inf'), float('+inf'))
