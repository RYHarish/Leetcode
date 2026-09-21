class Solution(object):
    def isbipartiate(self, graph, n):
        colour = [-1] * n
        for i in range(1, n+1):
            if colour[i-1] == -1:
                if not self.bfs_check(graph, i, colour):
                    return False
        return True
    
    def bfs_check(self, graph, node, colour):
        que = deque([node])
        colour[node-1] = 0

        while que:
            curr_node = que.popleft()
            for neighbor in graph[curr_node]:
                if colour[neighbor-1] == -1:
                    colour[neighbor-1] = 1 - colour[curr_node-1]
                    que.append(neighbor)
                elif colour[neighbor-1] ==  colour[curr_node-1]:
                    return False
        return True


    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)

        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        return self.isbipartiate(graph, n)