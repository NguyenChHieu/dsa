class Solution:
    # djikstra with dp counting the ways to a certain node.
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for v1,v2,w in roads:
            graph[v1].append((v2, w))
            graph[v2].append((v1, w))
        
        dist = defaultdict(lambda: float('inf'))
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1

        heap = [(0, 0)]
        min_cost = float("inf")

        while heap:
            curr_dist, curr = heappop(heap)
            if curr_dist > dist[curr]:
                continue
           
            for nb, w in graph[curr]:
                new_dist = curr_dist + w
                
                # shorter path -> inherit all paths from curr
                if new_dist < dist[nb]:
                    ways[nb] = ways[curr]
                    dist[nb] = new_dist
                    heappush(heap, (new_dist, nb))
                # another path
                elif new_dist == dist[nb]:
                    ways[nb] = (ways[nb] + ways[curr]) % (10 ** 9 + 7)
        return ways[n-1]
