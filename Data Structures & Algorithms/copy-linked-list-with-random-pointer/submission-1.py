"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = {}
        r_orig = head
        r_copy = None
        new_head = None
        while r_orig:
            r_copy = cache.get(r_orig, Node(r_orig.val, None, None))
            if not new_head:
                new_head = r_copy
            cache[r_orig] = r_copy
            if r_orig.next:
                r_copy.next = cache.get(r_orig.next, Node(r_orig.next.val, None, None))
                cache[r_orig.next] = r_copy.next
            if r_orig.random:
                r_copy.random = cache.get(r_orig.random, Node(r_orig.random.val, None, None))
                cache[r_orig.random] = r_copy.random
            r_orig = r_orig.next
        return new_head





        