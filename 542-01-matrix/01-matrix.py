from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        ans = [[0]*cols for _ in range(rows)]
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]== 0:
                    queue.append((r,c))
                    visited.add((r,c))
        while queue:
            r,c = queue.popleft()
            directions = [(r+1,c),
            (r-1,c),
            (r,c+1),
            (r,c-1)]
            for nr,nc in directions:
                if (nr<0 or nr>=rows or nc<0 or nc>=cols):
                    continue
                if (nr,nc) in visited:
                    continue
                ans[nr][nc] = ans[r][c]+1
                visited.add((nr, nc))
                queue.append((nr, nc))
        return ans
