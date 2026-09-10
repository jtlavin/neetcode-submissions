# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root, depth_indent=0):
        if not root:
            print("  " * depth_indent + "None -> 0")
            return 0
        print("  " * depth_indent + f"entrando a nodo {root.val}")
        l = self.maxDepth(root.left, depth_indent + 1)
        r = self.maxDepth(root.right, depth_indent + 1)
        result = 1 + max(l, r)
        print("  " * depth_indent + f"saliendo de nodo {root.val}, devuelve {result}")
        return result
            