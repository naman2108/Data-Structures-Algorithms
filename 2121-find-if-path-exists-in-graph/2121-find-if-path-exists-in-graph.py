from typing import List

class Solution:
    def dfs(self, node, destination, visited, graph):
        if node == destination:
            return True
        
        visited[node] = True
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if self.dfs(neighbor, destination, visited, graph):
                    return True
        
        return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        
        return self.dfs(source, destination, visited, graph)
