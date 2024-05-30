# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diff = 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self._dfs(root)
        return self.max_diff <= 1
        
        # compare max depth of left and right using dfs and ensure the root node has less than a 1 diff

    def _dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        left_depth = self._dfs(root.left)
        right_depth = self._dfs(root.right)

        # check max diff between the left and right paths
        self.max_diff = max(self.max_diff, abs(left_depth - right_depth))

        # return the longest depth observed so far
        return 1 + max(left_depth, right_depth)
