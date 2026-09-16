class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                e = board[r][c]
                if e == ".":
                    continue
                if e in rows[r] or e in cols[c] or e in squares[(r // 3, c // 3)]:
                    return False
                rows[r].add(e)
                cols[c].add(e)
                squares[(r // 3, c // 3)].add(e)
        return True

