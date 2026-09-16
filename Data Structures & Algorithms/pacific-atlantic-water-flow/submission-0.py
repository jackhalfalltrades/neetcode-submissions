class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        pac, atl = set(), set()
        res = []
        def dfs(r, c, visit, prevHeight):
            if (r not in range(ROWS)
                or c not in range(COLS)
                or grid[r][c] < prevHeight
                or (r, c) in visit
            ):
                return
            visit.add((r,c))
            dfs(r + 1, c , visit, grid[r][c])
            dfs(r - 1, c , visit, grid[r][c])
            dfs(r, c + 1 , visit, grid[r][c])
            dfs(r, c - 1 , visit, grid[r][c])
        for c in range(COLS):
            dfs(0, c, pac, grid[0][c])
            dfs(ROWS - 1 , c, atl, grid[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, grid[r][0])
            dfs(r, COLS - 1, atl, grid[r][COLS - 1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res