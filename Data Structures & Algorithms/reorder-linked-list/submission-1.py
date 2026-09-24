# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        if not head.next:
            return

        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        l1 = head
        l2 = slow

        # reverse l2
        prev = None
        while l2:
            n = l2.next
            l2.next = prev
            prev = l2
            l2 = n

        l2 = prev
        last = None
        while l1 or l2:
            l1_next = l1.next if l1 else None
            l2_next = l2.next if l2 else None

            if l1:
                l1.next = l2                
                l2.next = l1_next
                l1 = l1_next
                last = l2
                l2 = l2_next
            else:
                last.next = l2
                l2 = l2_next

