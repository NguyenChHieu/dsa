class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # simply perform dfs on the nodes ascendingly
        # at any time a cycle was found, that means the nodes involved
        # in the cycle will never be able to reached a terminal node -> unsafe
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            # check every path if they ended with term nodee
            for nb in graph[i]:
                if not dfs(nb):
                    return safe[i] # by default safe[i] marked to False
            safe[i] = True
            return safe[i]

        safe = {}
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
