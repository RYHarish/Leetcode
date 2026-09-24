from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        distance = [float('inf')] * (n + 1)
        distance[k] = 0
        pq = [(0, k)]
        visited = [False] * (n + 1)

        while pq:
            d, u = heapq.heappop(pq)

            if visited[u]:
                continue
            
            visited[u] = True

            for neighbor, weight in graph[u]:
                if not visited[neighbor] and distance[neighbor] > d + weight:
                    distance[neighbor] = d + weight
                    heapq.heappush(pq, (distance[neighbor], neighbor))
        
        max_delay = max(distance[1:])
        
        return max_delay if max_delay != float('inf') else -1
