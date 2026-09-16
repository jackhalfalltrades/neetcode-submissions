class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque() #r, c, and dist

        def capture(r, c):
            if(
                r not in range(ROWS)
                or c not in range(COLS)
                or (r, c) in visit
                or grid[r][c] == -1
                ):
                return
            visit.add((r, c))
            q.append((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r , c))
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                capture(r + 1, c)
                capture(r - 1, c)
                capture(r, c + 1)
                capture(r, c - 1)
            dist += 1

