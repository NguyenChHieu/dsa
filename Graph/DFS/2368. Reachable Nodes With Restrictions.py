class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # construct
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        def dfs(node):
            for nb in graph[node]:
                if nb not in restricted and nb not in seen:
                    seen.add(nb)
                    dfs(nb)

        restricted = set(restricted)
        seen = set()
        seen.add(0)
        dfs(0)
        return len(seen)
