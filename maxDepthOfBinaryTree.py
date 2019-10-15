# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None or root.val == None:
            return 0
        
        depth = 1
        q = deque()
        q.append((root,1)) #store tuple with node & current depth of node
        
        while(len(q)!=0):
            node = q.popleft()
            left = node[0].left
            right = node[0].right
            curr = node[1]
            
            if left!=None:
                q.append((left,curr+1))
            if right!=None:
                q.append((right,curr+1))
                
            depth = max(depth, curr)
            
        return depth
