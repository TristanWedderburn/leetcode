# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root or root.val == None:
            return []
        
#         initial BFS attempt
#         levels = []
#         q = deque() 
#         q.append((root,0))
        
#         while q:
#             curr = q.popleft()
#             node = curr[0]
#             level = curr[1]
            
#             if len(levels) > level:
#                 levels[level].append(node.val)
#             else:
#                 levels.append([node.val])
                
#             left = node.left
#             right = node.right
            
#             if node.left:
#                 q.append((node.left, level+1))
#             if node.right:
#                 q.append((node.right, level+1))

#         return levels

        levels = []
        level = 0
        q = deque([root]) 
    
        while q:
            levels.append([])
            level_length = len(q) # how many elements there are in the current level
        
            for i in range(level_length): # instead of tracking the levels, pop all of the elements in the q which should represent a whole level of nodes
                node = q.popleft()
                levels[level].append(node.val) #add current node to the current level array
                
                #add all of the children of current node to the q for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return levels
