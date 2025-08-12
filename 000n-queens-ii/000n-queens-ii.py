class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols = set()
        diagonals = set()        # row - col
        anti_diagonals = set()   # row + col

        def backtrack(row):
            if row == n:
                return 1

            count = 0
            for col in range(n):
                if col in cols or (row - col) in diagonals or (row + col) in anti_diagonals:
                    continue

                # Place queen
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)

                count += backtrack(row + 1)

                # Remove queen (backtrack)
                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

            return count

        return backtrack(0)