class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # ~ find the vertices with indegree = 0
        # this is because there is no way to access these nodes without starting from them.

        # edge cases: if the graph is simply a cycle -> the algo would return 0 -> but
        # the given graph is acyclic so no need to handle.

        indegree = [0] * n
        for _, indeg in edges:
            indegree[indeg] += 1

        return [node for node in range(n) if indegree[node] == 0]
