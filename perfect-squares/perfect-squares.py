import math
from collections import deque

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        
        queue = deque([(n, 0)]) 
        visited = set()
        
        while queue:
            remaining, turns = queue.popleft()
        
            if remaining == 0:
                return turns
            
            for square in nums:
                if remaining - square < 0:
                    break

                new_remaining = remaining - square
                if new_remaining not in visited:
                    visited.add(new_remaining)
                    queue.append((new_remaining, turns + 1))