class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x1, y1 = self.find(x), self.find(y)
        if x1 == y1:
            return False
        if self.rank[x1] > self.rank[y1]:
            self.parent[y1] = x1
            self.rank[x1] += self.rank[y1]
        else:
            self.parent[x1] = y1
            self.rank[y1] += self.rank[x1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        mail_id = {}
        for i, account in enumerate(accounts):
            for mail in account[1:]:
                if mail in mail_id:
                    uf.union(i, mail_id[mail])
                else:
                    mail_id[mail] = i
        id_mails = defaultdict(list)
        for mail, i in mail_id.items():
            parent = uf.find(i)
            id_mails[parent].append(mail)
        res = []
        for i, mails in id_mails.items():
            name = accounts[i][0]
            res.append([name] + sorted(mails))
        return res