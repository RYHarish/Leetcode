from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = '0'  
            
            while queue:
                x, y = queue.popleft()
                for direction in directions:
                    new_x, new_y = x + direction[0], y + direction[1]
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == '1':
                        grid[new_x][new_y] = '0'  
                        queue.append((new_x, new_y))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1': 
                    island_count += 1
                    bfs(r, c)
        
        return island_count