class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        queue = []
        
        visited = set()
        queue.append(rooms[0])
        visited.add(0)
        
        while queue:
            
            ele = queue.pop(0)
            for e in ele:
                if e not in visited:
                    queue.append(rooms[e])
                    visited.add(e)
                    if len(visited) == len(rooms):
                        return True
        
        return False