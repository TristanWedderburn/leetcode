# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None or root.val == None:
            return True
        
        stack = []
        min = float('-inf')
        
        while(len(stack)!=0 or root!=None):
            while root!=None: #add all nodes in left subtree
                stack.append(root)
                root = root.left
            root = stack.pop() #visit center node
            if root.val <= min:
                return False
            min = root.val #all nodes in in order traversal must be greater than the last node i.e the leftmost must be the smallest value
            root = root.right # check right subtree
                
        return True
