class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh, timeToRot = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if(row in range(ROWS) and col in range(COLS) and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))
            timeToRot += 1
        return timeToRot if fresh == 0 else -1