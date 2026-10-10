from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lands = set()
        m = len(grid)
        n = len(grid[0])

        def get_land_neighbors(cell):
            res = []
            i, j = cell

            top = (i - 1) * n + j
            bottom = (i + 1) * n + j
            left = (i) * n + j - 1
            right = (i) * n + j + 1


            if 0<=i-1<m and top in lands:
                res.append(top)
            if 0 <= i + 1 < m and bottom in lands:
                res.append(bottom)
            if 0<=j-1<n and left in lands:
                res.append(left)
            if 0<=j+1<n and right in lands:
                res.append(right)
            return res

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    lands.add(i * n + j)

        island_count = 0
        while len(lands) > 0:
            land_pos: int = lands.pop()
            island_count += 1
            l_i, l_j = land_pos // n, land_pos % n
            lq = deque()
            lq.append((l_i, l_j))

            while lq:
                land: tuple = lq.pop()
                neighbors = get_land_neighbors(land)
                for pos in neighbors:
                    lands.remove(pos)
                    lq.append((pos // n, pos % n))
        return island_count
