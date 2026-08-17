class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbours in adj[node]:
                if neighbours not in visited:
                    dfs(neighbours)
        dfs(source)
        return destination in visited