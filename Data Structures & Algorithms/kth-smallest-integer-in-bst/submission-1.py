# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        contador = k
        resultado = None
        def dfs(node):
            nonlocal contador, resultado
            if not node:
                return
            if resultado is not None:
                return
            
            dfs(node.left)
        
            contador -= 1
            if contador==0:
                resultado = node.val
                return
            dfs(node.right)

        dfs(root)
        return resultado
        