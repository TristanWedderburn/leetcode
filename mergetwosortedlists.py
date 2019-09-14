# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         result = result_tail = ListNode(0)
        
#         while(l1 and l2):
#             val = 0
#             if(l1.val<=l2.val):
#                 val = l1.val
#                 l1 = l1.next
#             else:
#                 val = l2.val
#                 l2 = l2.next
#             result_tail.next = ListNode(val)
#             result_tail = result_tail.next
        
#         if(l1 or l2):
#             result_tail.next = l2 if l1 == None else l1
        
#         return result.next

# we can optimize solution even more by using constant space and just reassigning the links of all of the nodes using the result_tail node
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = result_tail = ListNode(0)
        
        while(l1 and l2):
            if(l1.val<=l2.val):
                result_tail.next = l1
                l1 = l1.next
            else:
                result_tail.next = l2
                l2 = l2.next
            result_tail = result_tail.next
        
        if(l1 or l2):
            result_tail.next = l2 if l1 == None else l1
        
        return result.next
