class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        color  = [-1] * len(graph)
        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    color[neighbour] = 1-color[node]
                    if dfs(neighbour):
                        return True
                elif color[neighbour] == color[node]:
                    return True
            return False
        for start in range(len(graph)):
            if start not in visited:
                color[start] = 0
                if dfs(start):
                    return False
        return True