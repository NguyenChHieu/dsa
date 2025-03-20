class Solution:
    # a & b will either keep the number the same or decrease it
    # dfs through all components, map each node to the corresponding
    # component number. Just simply loop through all edges and then
    # compute the component's value.
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        def dfs(node, compNum):
            for nb in graph[node]:
                if nb not in seen:
                    compMap[nb] = compNum
                    seen.add(nb)
                    dfs(nb, compNum)
        # construct graph
        graph = {i: [] for i in range(n)}
        for v1,v2,_ in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        # map components
        seen = set()
        comp = 0
        compMap = {i: 0 for i in range(n)}
        for node in range(n):
            if node not in seen:
                comp += 1
                compMap[node] = comp
                seen.add(node)
                dfs(node, comp)

        # compute the component value
        MAX_VALUE = 2**31 - 1
        size = {i+1:MAX_VALUE for i in range(comp)}
        for v1, v2, cost in edges:
            size[compMap[v1]] &= cost

        res = []
        for q1, q2 in query:
            if compMap[q1] == compMap[q2]:
                res.append(size[compMap[q1]])
            else:
                res.append(-1)
        return res
