# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use pointer to track what the last node was before overwriting it

        prev: Optional[ListNode] = None

        while (head): # continue iterating until reach end of linked list
            tmp = head.next # store old .next
            head.next = prev # set new .next
            prev = head # mark as seen
            head = tmp # process old .next
        
        return prev
