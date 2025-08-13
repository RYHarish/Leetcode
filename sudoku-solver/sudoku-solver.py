class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Pre-fill sets and collect empty cells
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    empty_cells.append((i, j))
                else:
                    val = int(val)
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)

        def backtrack(index):
            if index == len(empty_cells):
                return True  # Solved

            i, j = empty_cells[index]
            box_id = (i // 3) * 3 + (j // 3)

            for d in range(1, 10):
                if d not in rows[i] and d not in cols[j] and d not in boxes[box_id]:
                    board[i][j] = str(d)
                    rows[i].add(d)
                    cols[j].add(d)
                    boxes[box_id].add(d)

                    if backtrack(index + 1):
                        return True

                    # Backtrack
                    board[i][j] = "."
                    rows[i].remove(d)
                    cols[j].remove(d)
                    boxes[box_id].remove(d)

            return False

        backtrack(0)