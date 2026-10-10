from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def get_fresh_neighbors(cell):
            i, j = cell
            res = []
            if (0 <= i - 1 < m) and grid[i - 1][j] == 1:
                res.append([i - 1, j])
            if (0 <= i + 1 < m) and grid[i + 1][j] == 1:
                res.append([i + 1, j])
            if (0 <= j - 1 < n) and grid[i][j - 1] == 1:
                res.append([i, j - 1])
            if (0 <= j + 1 < n) and grid[i][j + 1] == 1:
                res.append([i, j + 1])
            return res

        fresh_count = 0
        rotten_fruits = deque()
        level = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    level.append((i, j))
        if level:
            rotten_fruits.append(level)

        minutes = -1
        rotten_count = len(rotten_fruits)
        original_fresh_count = int(fresh_count)
        empty_count = m * n - original_fresh_count - rotten_count
        while rotten_fruits:
            popped_level = rotten_fruits.popleft()
            minutes += 1
            level = deque()
            while popped_level:
                cell = popped_level.popleft()
                neighbors = get_fresh_neighbors(cell)
                for i, j in neighbors:
                    grid[i][j] = 2
                    fresh_count -= 1
                    level.append((i, j))
            if level:
                rotten_fruits.append(level)
        if not fresh_count and original_fresh_count!=0:
            return minutes
        elif not original_fresh_count:
            return 0
        else:
            return -1
