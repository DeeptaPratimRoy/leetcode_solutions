class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        color = [-1] * len(graph)
        def dfs(node):
            visited.add(node)
            for neighbours in graph[node]:
                if neighbours not in visited:
                    color[neighbours] = 1- color[node]
                    if dfs(neighbours):
                        return True
                elif color[neighbours] == color[node]:
                    return True
            return False
        for i in range(len(graph)):
            if i not in visited:
                color[i] = 0
                if dfs(i):
                    return False
        return True



        