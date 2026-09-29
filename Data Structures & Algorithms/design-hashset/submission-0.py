class MyHashSet:

    def __init__(self):
        self.check = []

    def add(self, key: int) -> None:
        self.check.append(key)

    def remove(self, key: int) -> None:
        while key in self.check:
            self.check.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.check


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)