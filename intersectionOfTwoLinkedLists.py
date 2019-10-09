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
        if not headA or not headB:
            return None
        
        setA = set()
        
        pA = headA
        while(pA!=None):
            setA.add(pA)
            pA=pA.next
        
        pB = headB
        while(pB!=None):
            if pB in setA:
                return pB
            pB=pB.next
        return None
