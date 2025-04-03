class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for x,y in roads:
            graph[x].add(y)
            graph[y].add(x)
        
        ans = 0
        for x in graph.keys():
            for y in graph.keys():
                if x == y:
                    continue
                if x in graph[y]:
                    ans = max(ans, len(graph[y]) + len(graph[x]) -1)
                else:
                    ans = max(ans, len(graph[y]) + len(graph[x]))
        return ans
            
