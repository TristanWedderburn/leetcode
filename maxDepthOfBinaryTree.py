# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursion
        # base case is return 0
        # recursive case is return 1 + max of maxDepth on left node and right node

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
