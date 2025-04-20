class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        for e1, e2 in edges:
            graph[e2].append(e1)
        
        def dfs(node, visited, ancest):
            visited.add(node)
            for parent in graph[node]:
                if parent not in visited:
                    ancest.add(parent)
                    dfs(parent, visited, ancest)
        ans = [[] for i in range(n)]

        for i in range(n):
            s = set()
            ancestor = set()
            dfs(i, s, ancestor)
            ans[i] = list(sorted(ancestor)) 
        return ans

        
