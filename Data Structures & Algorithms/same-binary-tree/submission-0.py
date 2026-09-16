# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Nos piden comparar 2 arboles
        # Opcion 1: recorrer ambos y guardar valores en una lista, luego comparar las listas
        # Podemos usar recursion, pero nos obliga a recorrer ambos arboles enteros

        # Opcion 2: ir comparando todo el tiempo y si encontramos un valor != salimos con un False
        # En el peor de los casos, recorremos entero el arbol mas pequeño
        if p is None and q is None:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        


