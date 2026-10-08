from collections import deque


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.row_count = len(grid)
        self.col_count = len(grid[0])
        self.perimeter = 0

        # Traversal logic
        dq = deque()
        src_i, src_j = self.get_src()
        dq.append([src_i, src_j])
        visited = [[False] * self.col_count for _ in range(self.row_count)]
        visited[src_i][src_j] = True

        while dq:
            land = dq.popleft()
            neighbors = self.get_land_neighbors(land)
            self.perimeter += 4 - len(neighbors)
            for cell in neighbors:
                i, j = cell
                if not visited[i][j]:
                    dq.append(cell)
                    visited[i][j] = True
        return self.perimeter

    def is_land_cell(self, cell: tuple[int, int]):
        i, j = cell
        return (0 <= i < self.row_count) and (0 <= j < self.col_count) and self.grid[i][j] == 1

    def get_land_neighbors(self, cell):
        land_parcels = []
        i, j = cell

        top = i - 1, j
        bottom = i + 1, j
        left = i, j - 1
        right = i, j + 1

        neighbors = [top, left, bottom, right]
        for cell in neighbors:
            if self.is_land_cell(cell):
                land_parcels.append(cell)

        return land_parcels

    def get_src(self):
        m = len(self.grid)
        n = len(self.grid[0])
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == 1:
                    return i, j
