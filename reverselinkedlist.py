# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# add in front of linked list
# linear time and constant space as we just allocate one node and then rearrange nodes of original linked list

class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         result = ListNode(0) #dummy node
#         self.reverseList_(head, result)
#         return result.next
    
#     def reverseList_(self, head, result):
#         if not head:
#             return None #function modifies result so we can just return none here to end the loop
        
#         rest = result.next 
#         result.next = head
#         store = head.next
#         result.next.next = rest
#         self.reverseList_(store, result)

# better recursive solution

#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
        
#         p = self.reverseList(head.next) # stack level recurses all the way to the end and then returns last element along the way
#         head.next.next = head #next element's.next points to head so that head actually follows head.next
#         head.next = None #last element (head) will point to None
#         return p #return last element as new head
        
# iterative solution
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while(curr):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            
        return prev
