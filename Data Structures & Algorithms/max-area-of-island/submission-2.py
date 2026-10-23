class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        unvisited = set()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    unvisited.add((i, j))

        def get_neighbors(cell):
            i, j = cell
            res = []
            if 0 <= i - 1 < m and grid[i - 1][j] == 1:
                res.append((i - 1, j))

            if 0 <= i + 1 < m and grid[i + 1][j] == 1:
                res.append((i + 1, j))

            if 0 <= j - 1 < n and grid[i][j - 1] == 1:
                res.append((i, j - 1))

            if 0 <= j + 1 < n and grid[i][j + 1] == 1:
                res.append((i, j + 1))

            return res

        self.max_area = 0

        def dfs(src):
            stk = [src]
            area = 0
            while stk:
                v = stk.pop()
                if v in unvisited:
                    unvisited.remove(v)
                area += 1
                for neighbor in get_neighbors(v):
                    if neighbor in unvisited:
                        stk.append(neighbor)
                        neighbor in unvisited and unvisited.remove(neighbor)
            self.max_area = max(self.max_area, area)

        while unvisited:
            dfs(unvisited.pop())

        return self.max_area
