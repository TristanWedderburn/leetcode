# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self._dfs(root)
        return self.max_diameter
    
    def _dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # starting at each node, try to find the max diameter while looking at the left + right
        left_diameter = self._dfs(root.left)
        right_diameter = self._dfs(root.right)

        # check if new global max diameter
        self.max_diameter = max(self.max_diameter, left_diameter + right_diameter)

        # return local max diameter
        return 1 + max(left_diameter, right_diameter)
    
