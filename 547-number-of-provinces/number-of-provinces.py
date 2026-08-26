class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = [[] for _ in range(n)] 
        for i in range(n):
            for u  in range(n):
                for v in range(n):
                    if isConnected[u][v] == 1:
                        adj[u].append(v)
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbours in adj[node]:
                if neighbours not in visited:
                    dfs(neighbours)
        count = 0
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)
        return count









