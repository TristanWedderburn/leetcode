# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs at the same time and check if the nodes are the same?
        # dfs and add all of the nodes we traversed to a list and then compare the lists?

        if not p and not q: # check if both null, same
            return True
        elif (p and not q) or (not p and q) or (p and q and p.val != q.val): # check if only one null or not same value, not same
            return False
        
        return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # current nodes are same, but check children
