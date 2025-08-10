class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque

        row, col = len(mat), len(mat[0])
        result = [[-1] * col for _ in range(row)]
        queue = deque()

        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    result[r][c] = 0
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and result[nr][nc] == -1:
                    result[nr][nc] = result[r][c] + 1
                    queue.append((nr, nc))

        return result