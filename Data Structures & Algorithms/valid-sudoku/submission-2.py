class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subBoxes = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if not board[i][j].isdigit():
                    continue

                num = int(board[i][j])
                if num in rows[i] or num in cols[j] or num in subBoxes[i // 3][j // 3]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                subBoxes[i // 3][j // 3].add(num)
        return True