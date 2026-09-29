class FirstUnique:

    def __init__(self, nums: List[int]):
        self.num_occuerence = {}
        self.occuerence_num = {}
        for x in nums:
            self.add(x)

    def showFirstUnique(self) -> int:
        if 1 in self.occuerence_num:
            return self.occuerence_num[1][0]
        return -1
        

    def add(self, value: int) -> None:
        if value in self.num_occuerence:
            y_old = self.num_occuerence[value]
            y_new = y_old + 1
            if value in self.occuerence_num.get(y_old, []):
                self.occuerence_num[y_old].remove(value)
                if not self.occuerence_num[y_old]:
                    del self.occuerence_num[y_old]
            
            if y_new not in self.occuerence_num:
                self.occuerence_num[y_new] = []
            
            self.occuerence_num[y_new].append(value)
            self.num_occuerence[value] = y_new
        else:
            self.num_occuerence[value] = 1
            if 1 not in self.occuerence_num:
                self.occuerence_num[1] = []
            self.occuerence_num[1].append(value)