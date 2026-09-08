class MyHashSet:

    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.data.append(key)

    def remove(self, key: int) -> None:
        idx = -1
        for i in range(len(self.data)):
            if self.data[i] == key:
                idx = i
                break
        if idx != -1:
            self.data[i], self.data[-1] = self.data[-1], self.data[i]
            self.data.pop()

    def contains(self, key: int) -> bool:
        return key in self.data
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)