class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        col_count = len(grid[0])
        perimeter = 0
        for i in range(row_count):
            for j in range(col_count):
                cell_perimeter = 4
                if grid[i][j] == 1:
                    # top
                    if (0 <= i - 1 < row_count) and grid[i - 1][j] == 1:
                        cell_perimeter -= 1
                    # bottom
                    if (0 <= i + 1 < row_count) and grid[i + 1][j] == 1:
                        cell_perimeter -= 1
                    # left
                    if (0 <= j - 1 < col_count) and grid[i][j - 1] == 1:
                        cell_perimeter -= 1
                    # right
                    if (0 <= j + 1 < col_count) and grid[i][j + 1] == 1:
                        cell_perimeter -= 1
                    perimeter += cell_perimeter
        return perimeter
