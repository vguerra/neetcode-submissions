# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = l1
        r2 = l2
        r_head = None
        prev = None
        carry = 0
        while r1 or r2 or carry > 0:
            op1 = r1.val if r1 else 0
            op2 = r2.val if r2 else 0

            add = op1 + op2 + carry
            # carry = (op1 & op2) << 1
            carry = 1 if add >= 10 else 0

            node = ListNode(add % 10)
            if not prev:
                r_head = node
            else:
                prev.next = node
            prev = node
            r1 = r1.next if r1 else None
            r2 = r2.next if r2 else None


        return r_head
        