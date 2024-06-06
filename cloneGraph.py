"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.nodeToClone = {}
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # dfs or bfs
        # use a map to track seen nodes for cycles
        if not node:
            return None
        
        # if in graph, return node
        if node in self.nodeToClone.keys():
            return self.nodeToClone.get(node)

        # clone and store in map
        clone = Node(node.val)
        self.nodeToClone[node] = clone

        # iterate neighbors
        for n in node.neighbors:
            clone.neighbors.append(self.cloneGraph(n))

        # return clone
        return clone
        
