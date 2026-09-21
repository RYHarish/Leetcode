class Solution(object):
    def dfs_check(self, graph, node, colour):
        for n in graph[node]:
            if colour[n] == -1:
                colour[n] = 1 - colour[node] 
                if not self.dfs_check(graph, n, colour):
                    return False
            elif colour[n] == colour[node]:
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
                colour[node] = 0
                if not self.dfs_check(graph, node, colour):
                    return False
        
        return True
    

