class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for v1,v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        def dfs(node):
            for nb in graph[node]:
                if nb not in seen:
                    seen.add(nb)
                    dfs(nb)
        
        ans = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)
        return ans
