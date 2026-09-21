class Solution(object):
    def bfs_check(self, graph, colour, node):
        
        que = deque([node])
        colour[node] = 0
        while que:
            node = que.pop()
            neighbors = graph[node]
            for neighbor in neighbors:
                if colour[neighbor] == -1:
                    colour[neighbor] = 1 - colour[node]
                    que.append(neighbor)
                if colour[neighbor] == colour[node]:
                    return False
        return True

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        colour = [-1] * n
        for node in range(n):
            if colour[node] == -1:
                if not self.bfs_check(graph, colour, node):
                    return False
        return True
        

        