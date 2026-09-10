# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-1, None)

        prev = sentinel
        runner1 = list1
        runner2 = list2

        while runner1 is not None or runner2 is not None:
            if runner1 is None:
                prev.next = runner2
                runner2 = runner2.next
            elif runner2 is None:
                prev.next = runner1
                runner1 = runner1.next
            elif runner1.val < runner2.val:
                prev.next = runner1
                runner1 = runner1.next
            else:
                prev.next = runner2
                runner2 = runner2.next
            prev = prev.next
        
        return sentinel.next



        