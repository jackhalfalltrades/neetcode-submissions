class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        if not grid or not grid[0]:
            return islands
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        def dfs(r, c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or grid[r][c] == "0" 
                or (r, c) in visit):
                return
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in visit:
                    islands += 1
                    dfs(i, j)
        return islands