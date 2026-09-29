class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj_list = defaultdict(list)

        for e1, e2 in edges:
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)
        visit = set()
        def dfs(node, prev):
            visit.add(node)

            for nextNode in adj_list[node]:
                if nextNode == prev:
                    continue
                if nextNode in visit:
                    return False
                if not dfs(nextNode, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n