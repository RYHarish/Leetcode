from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadend_set = set(deadends)
        if "0000" in deadend_set:
            return -1  
        
        queue = deque([("0000", 0)]) 
        visited = set("0000")
        
        while queue:
            current, turns = queue.popleft()
            
            if current == target:
                return turns
            
            for i in range(4):
                for move in [-1, 1]:
                    next_wheel = (int(current[i]) + move) % 10
                    next_state = current[:i] + str(next_wheel) + current[i+1:]
                    
                    if next_state not in deadend_set and next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, turns + 1))
        
        return -1