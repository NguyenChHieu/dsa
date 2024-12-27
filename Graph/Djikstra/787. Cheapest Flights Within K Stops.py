class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for v1, v2, w in flights:
            graph[v1].append((v2, w))

        heap = [(0, 0, src)]
        # tracks dist to (node, curr_k), allowing a node can have multiple states base on k
        min_cost = defaultdict(lambda: float('inf')) 
        min_cost[(src, 0)] = 0

        while heap:
            curr_dist, curr_k, curr_node = heappop(heap)
            if curr_node == dst:
                return curr_dist
            if curr_k > k:
                continue
            for nb, weight in graph[curr_node]:
                distance = curr_dist + weight
                # it potentially accepts the paths which might have
                # distance that currently > min_cost[node], but
                # it might produce the shorter path to the dst (thanks to the heap)
                if distance < min_cost[(nb,curr_k+1)]:
                    min_cost[(nb,curr_k+1)] = distance
                    heappush(heap, (distance, curr_k+1, nb))
        return -1
                
