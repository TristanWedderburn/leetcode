# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
#         time: O(max(n,m))
#         space: O(max(n))
#         if not headA or not headB:
#             return None
        
#         setA = set()
        
#         pA = headA
#         while(pA!=None):
#             setA.add(pA)
#             pA=pA.next
        
#         pB = headB
#         while(pB!=None):
#             if pB in setA:
#                 return pB
#             pB=pB.next
#         return None
# in order to reduce the space complexity of the solution, we can traverse the linked list twice. 
# Since both of the linked lists have the same ending, the quicker solution restart the list quicker
# in order to offset the list indexing and find the intersected nodes.
# time: O(n+m)
# space: O(1)
        pA = headA
        pB = headB
        while(pA!=pB):
            pA = pA.next if pA!=None else headB
            pB = pB.next if pB!=None else headA
        return pA
