# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n) time and space
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

# O(n) time, O(1) space
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         if not head:
#             return False
        
#         slow = head
#         fast = head.next
        
#         while(slow and fast):
#             if slow == fast:
#                 return True
            
#             if fast.next and fast.next.next:
#                 fast = fast.next.next
#                 slow = slow.next
#             else:
#                 return False
#         return False
        
