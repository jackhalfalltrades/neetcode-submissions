class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        def dfs(r, c, i):
            if len(word) == i:
                return True
            if (r == ROWS or c == COLS or r < 0 or c < 0 or board[r][c] != word[i] or (r,c) in visit):
                return False
            visit.add((r,c))
            res = (dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1))
            visit.remove((r, c))
            return res
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False

