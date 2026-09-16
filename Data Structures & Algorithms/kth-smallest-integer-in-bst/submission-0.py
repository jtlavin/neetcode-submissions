# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Nos dan un BST ordenado
        # Eso significa que si recorremos de izquierda a derecha siempre el numero debe ir subiendo
        # Debemos recorrer de izquierda a derecha contando los nodos
        # Cuando lleguemos al nodo kth, ese será el elemento kth mas pequeño ya que siempre vamos subiendo
        valores = []
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            valores.append(node.val)
            inorder(node.right)

        inorder(root)
        return valores[k-1]
