# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # iterate on root until we reach node with subRoot head
        # call inner DFS to compare two roots from then on
        if not root:
            return None
        
        found_sub_tree = False

        if root.val == subRoot.val: # If the current nodes have the same value, test 
            found_sub_tree = self._is_same_tree(root, subRoot)
        
        return found_sub_tree or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) # check if found or any of the subtrees have found it
    
    def _is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (not p and q) or (p and not q) or (p and q and p.val != q.val):
            return False
        
        return True and self._is_same_tree(p.left, q.left) and self._is_same_tree(p.right, q.right)
