class Solution: 
    def isBipartite(self, graph: List[List[int]]) -> bool: 
        visited = set() 
        color = [-1] * len(graph) 
        def dfs(node): 
            visited.add(node) 
            for nei in graph[node]: 
                if nei not in visited: 
                    color[nei] = 1 - color[node] 
                    if not dfs(nei): 
                        return False 
                elif color[nei] == color[node]: 
                    return False 
            return True 
        for i in range(len(graph)): 
            if i not in visited: 
                color[i] = 0 
                if not dfs(i): 
                    return False  
        return True 