class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for v1, v2, weight in times:
            graph[v1].append((v2, weight))

        dist = [float('inf')] * n
        # source
        dist[k-1] = 0 # 0-idx
        heap = [(0, k)]
        ans = 0

        while heap:
            curr_dist, curr_node = heappop(heap)
            if curr_dist > dist[curr_node-1]: # 0-idx
                continue

            for nxt_node, weight in graph[curr_node]:
                distance = curr_dist + weight
                if distance < dist[nxt_node-1]: # 0-idx
                    dist[nxt_node-1] = distance # 0-idx
                    heappush(heap, (distance, nxt_node))

        # check any node that was not reached
        for d in dist:
            if d == float('inf'):
                return -1
            else:
                ans = max(ans, d)
        return ans
