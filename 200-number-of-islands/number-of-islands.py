from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        def bfs(r,c):
            queue = deque([(r,c)])
            visited[r][c] = True
            while queue:
                r,c = queue.popleft()
                directions = [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1)
                ]
                for nr,nc in directions:
                    if(
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == "1"
                        and not visited[nr][nc]
                    ):
                        visited[nr][nc] = True
                        queue.append((nr,nc))
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    count += 1
                    bfs(r, c)
        return count

        