# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        count = 1
        right_count = count + self.maxDepth(root.right)
        left_count = count + self.maxDepth(root.left)
        if right_count > left_count:
            return right_count
        else:
            return left_count

        
        