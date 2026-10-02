class LRUCache:
    class CacheNode:
        def __init__(self, key: int, value: int, prev: CacheNode | None, next: CacheNode | None):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = None
        self.mru = None
        self.key_to_node = dict()
    
    def _remove(self, node: CacheNode) -> None:
        p = node.prev
        n = node.next

        if p:
            p.next = node.next
        if n:
            n.prev = p
        node.next = None
        node.prev = None

        if self.lru == node:
            self.lru = n
        if self.mru == node:
            self.mru = p
    
    def _insert(self, node: CacheNode) -> None:
        if self.mru:
            self.mru.next = node
        node.prev = self.mru
        self.mru = node

        if not self.lru:
            self.lru = node 


    def get(self, key: int) -> int:
        if not self.key_to_node or key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]

        self._remove(node)
        self._insert(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._remove(node)
        else:
            node = self.CacheNode(key, value, self.mru, None)
            self.key_to_node[key] = node

        if len(self.key_to_node) > self.capacity:
            self.key_to_node.pop(self.lru.key)
            self._remove(self.lru)

        self._insert(node)

        return
