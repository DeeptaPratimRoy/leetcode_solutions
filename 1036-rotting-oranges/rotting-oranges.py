from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        row = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = set()
        fresh = 0
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        time = 0
        while queue and fresh > 0:
            n = len(queue)
            for i in range(n):
                r, c = queue.popleft()
                directions = [
                    (r+1, c),
                    (r-1, c),
                    (r, c+1),
                    (r, c-1)
                ]
                for nr, nc in directions:
                    if nr < 0 or nr >= row or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] == 1 and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        fresh -= 1
            time += 1
        if fresh > 0:
            return -1
        return time