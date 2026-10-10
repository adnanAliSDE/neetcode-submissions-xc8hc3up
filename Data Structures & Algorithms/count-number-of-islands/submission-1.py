from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lands = set()
        m = len(grid)
        n = len(grid[0])

        def get_land_neighbors(cell):
            res = []
            i, j = cell
            if 0 <= i - 1 < m and grid[i - 1][j] == "1":
                res.append((i-1, j))
            if 0 <= i + 1 < m and grid[i + 1][j] == "1":
                res.append((i+1, j))
            if 0 <= j - 1 < n and grid[i][j - 1] == "1":
                res.append((i, j-1))
            if 0 <= j + 1 < n and grid[i][j + 1] == "1":
                res.append((i, j+1))
            return res

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    lands.add(i * n + j)

        visited=[[False]*n for _ in range(m)]
        island_count = 0
        while len(lands)>0:
            land_pos:int = lands.pop()
            island_count += 1
            l_i, l_j = land_pos // n, land_pos % n
            lq = deque()
            lq.append((l_i, l_j))
            visited[l_i][l_j]=True

            while lq:
                land:tuple = lq.pop()
                neighbors = get_land_neighbors(land)
                for i, j in neighbors:
                    pos=i * n + j
                    if pos in lands:
                        lands.remove(pos)
                        lq.append((i,j))
        return island_count
