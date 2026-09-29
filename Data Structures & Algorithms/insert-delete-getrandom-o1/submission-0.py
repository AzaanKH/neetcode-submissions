class RandomizedSet:

    def __init__(self):
        self.check = set()
        

    def insert(self, val: int) -> bool:
        if val in self.check:
            return False
        self.check.add(val)
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.check:
            return False
        self.check.remove(val)
        return True
        

    def getRandom(self) -> int:
        random_element = random.choice(tuple(self.check))
        return random_element
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()