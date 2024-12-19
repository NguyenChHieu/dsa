class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for nb in graph[node]:
                if nb not in visited:
                    if dfs(nb, visited):
                        return True
            return False
        
        seen = {source}
        return dfs(source, seen)
