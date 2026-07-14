class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def backtrack(r,c,index):
            if index == len(word):
                return True
            if (r<0 or r>=rows or c<0 or c>=cols or board[r][c]!=word[index] or (r,c) in visited):
                return False

            visited.add((r,c))
            if (backtrack(r + 1, c, index + 1) or
                backtrack(r - 1, c, index + 1) or
                backtrack(r, c + 1, index + 1) or
                backtrack(r, c - 1, index + 1)):
                    return True

            visited.remove((r, c))
            return False
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True

        return False