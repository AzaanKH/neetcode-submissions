class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # go through n from 0 to n run dfs on it and if current node not in the visit set 
        # then increment components
        adj_list = defaultdict(list)
        visit = set()
        for e1, e2 in edges:
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)
        
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nextNode in adj_list[node]:
                if nextNode not in visit:
                    dfs(nextNode)
            return
        components = 0
        for node in range(n):
            if node not in visit:
                components += 1
                dfs(node)
        
        return components