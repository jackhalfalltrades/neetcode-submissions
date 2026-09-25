class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        visit = set()
        queue = deque()

        queue.append((0, 0))
        visit.add((0,0))

        path = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return path

                neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0],
                              [1, 1], [1, -1], [-1, 1], [-1, -1]]
                for dr, dc in neighbours:
                    nr = r + dr
                    nc = c + dc

                    if (
                        nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        (nr, nc) in visit or
                        grid[nr][nc] == 1
                    ):
                        continue

                    queue.append((nr, nc))
                    visit.add((nr, nc))
            path +=1
        return -1

