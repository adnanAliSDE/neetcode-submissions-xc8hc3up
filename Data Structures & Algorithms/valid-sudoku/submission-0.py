class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        t = [
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        m, n = 9, 9

        def get_flat_idx(i, j):
            return i * n + j

        table = {}
        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if not char.isdigit():
                    continue
                if not 1 <= int(char) <= 9:
                    return False
                indices = table.get(char, [])
                for pre_i, pre_j in indices:
                    if pre_i == i or pre_j == j or (pre_i // 3, pre_j // 3) == (i // 3, j // 3):
                        return False
                indices.append((i, j))
                table[char] = indices
        return True
