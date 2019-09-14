# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# add in front of linked list
# linear time and constant space as we just allocate one node and then rearrange nodes of original linked list

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        result = ListNode(0) #dummy node
        self.reverseList_(head, result)
        return result.next
    
    def reverseList_(self, head, result):
        if not head:
            return None #function modifies result so we can just return none here to end the loop
        
        rest = result.next 
        result.next = head
        store = head.next
        result.next.next = rest
        self.reverseList_(store, result)
