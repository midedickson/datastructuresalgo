# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root:
            if root.right or root.left:
                holder = root.right
                root.right = root.left
                root.left = holder
            if root.right:
                root.right = self.invertTree(root.right)
            if root.left:
                root.left = self.invertTree(root.left)
        return root