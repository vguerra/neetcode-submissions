# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        runner = head
        for _ in range(n):
            runner = runner.next
        prev = None
        to_delete = head
        while runner:
            runner = runner.next
            prev = to_delete
            to_delete = to_delete.next

        if not prev:
            return head.next            

        prev.next = to_delete.next

        return head
        