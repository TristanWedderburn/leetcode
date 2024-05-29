# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers
        # one pointer used as the head of the new linked list, head
        # one pointer to traverse, curr

        # compare current val of each list head
        # smaller is head
        # advance list
        # head, curr

        # loop compare current vals
        # smaller is curr.next
        # advance list
        # advance to curr.next

        # return head

        # handle empty lists
        if not list1:
            return list2
        elif not list2:
            return list1

        head = curr = None

        # figure out where to start merged list
        if list1.val <= list2.val:
            head = curr = list1
            list1 = list1.next
        else:
            head = curr = list2
            list2 = list2.next

        # iterate on each list
        while (list1 and list2):
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        
        # handle one list finishing before the other
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return head
