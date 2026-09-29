# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_node = None
        right_node = None

        runner = head
        prev = None
        prev_left = None
        after_right = None
        pos = 1
        while runner:
            if pos == left:
                left_node = runner
                prev_left = prev
            if pos == right:
                right_node = runner
                after_right = runner.next
            prev = runner
            runner = runner.next
            pos += 1
        
        if not left_node or not right_node:
            return head

        prev = None
        runner = left_node
        stop = right_node.next
        while runner != stop:
            next_node = runner.next
            runner.next = prev
            prev = runner
            runner = next_node

        if not prev_left:
            head = right_node
        else:
            prev_left.next = right_node
        left_node.next = stop

        return head
        