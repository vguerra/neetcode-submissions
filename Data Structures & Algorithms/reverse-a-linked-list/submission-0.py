# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        runner = head

        while runner:
            n = runner.next
            runner.next = prev
            prev = runner
            runner = n
        
        return prev

        