class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # construct the initial roads, then perform dfs from 0,
        # any edge that matches that in set roads are moving away from 0
        # so we have to flip it.

        roads = set() 
        graph = defaultdict(list)
        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x,y))
        
        def dfs(node):
            path = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node, neighbor) in roads:
                        path += 1
                    seen.add(neighbor)
                    path += dfs(neighbor)
            return path
        seen = {0}
        return dfs(0)
