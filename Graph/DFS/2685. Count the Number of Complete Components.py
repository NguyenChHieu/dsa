class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        compMap = defaultdict(list)
        compNum = 0
        seen = set()

        def dfs(node):
            for nb in graph[node]:
                if nb not in seen:
                    seen.add(nb)
                    compMap[compNum].append(nb)
                    dfs(nb)

        for node in range(n):
            if node not in seen:
                compNum += 1
                compMap[compNum].append(node)
                seen.add(node)
                dfs(node)

        ans = 0
        for i in range(1, compNum + 1):
            skip = False
            for node in compMap[i]:
                if len(graph[node]) != len(compMap[i]) - 1:
                    skip = True
                    break
            if not skip:
                ans += 1
        return ans
        

        
        
