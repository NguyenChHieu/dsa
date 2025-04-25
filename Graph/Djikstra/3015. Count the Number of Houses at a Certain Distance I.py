class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append([i + 1, 1])
            graph[i + 1].append([i,1])
        # 0 idx
        graph[x-1].append([y-1, 1])
        graph[y-1].append([x-1, 1])

        def djikstra(st):
            pq = [(st, 0)]
            dists = [float('inf')] * n
            dists[st] = 0
            while pq:
                node, dist = heappop(pq)
                for nb, w in graph[node]:
                    new_dist = dist + w
                    if nb != st and new_dist < dists[nb]:
                        dists[nb] = new_dist
                        heappush(pq, (nb, new_dist))
            return dists
        ans = [0] * n
        for i in range(n):
            dists = djikstra(i)
            for d in dists:
                if d:
                    ans[int(d)-1] += 1
        return ans
            

