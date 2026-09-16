class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        if not grid or not grid[0]:
            return maxArea
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        def dfs(r, c):
            if(
                r not in range(ROWS)
                or c not in range(COLS)
                or grid[r][c] == 0
                or (r, c) in visit
                ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visit:
                    maxArea = max(maxArea, dfs(i,j))
        return maxArea
