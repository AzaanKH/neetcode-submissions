class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        check = set()
        def dfs(node, parent):
            if node in check:
                return False
            check.add(node)
            for next in adj_list[node]:
                if next == parent:
                    continue
                if not dfs(next, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(check) == n