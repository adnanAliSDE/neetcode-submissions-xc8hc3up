from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        lands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    lands.add((i, j))

        def get_land_neighbors(cell):
            res = []
            i, j = cell

            top = (i - 1, j)
            bottom = (i + 1, j)
            left = (i, j - 1)
            right = (i, j + 1)

            if 0 <= top[0] < m and top in lands:
                res.append(top)
            if 0 <= bottom[0] < m and bottom in lands:
                res.append(bottom)
            if 0 <= left[1] < n and left in lands:
                res.append(left)
            if 0 <= right[1] < n and right in lands:
                res.append(right)
            return res

        island_count = 0
        while lands:
            lq = deque()
            lq.append(lands.pop())

            island_count += 1

            while lq:
                land: tuple = lq.popleft()
                neighbors = get_land_neighbors(land)
                for pos in neighbors:
                    lands.remove(pos)
                    lq.append(pos)
        return island_count
