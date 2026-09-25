from collections import deque
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if color == original_color:
            return image
        rows = len(image)
        cols = len(image[0])
        queue = deque([(sr, sc)])
        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            directions = [
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1)
            ]
            for nr, nc in directions:
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and image[nr][nc] == original_color
                ):
                    queue.append((nr, nc))
                    image[nr][nc] = color
        return image