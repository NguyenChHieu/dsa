class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # directed graph.
        # each bomb is a vertex, edge exists only when the vertices
        # are "close" enough to the vertex's radius

        # problem becomes bfs and find the largest connected compo.
        def toDist(x1, y1, x2, y2):
            return float(sqrt((x1-x2)**2 + (y1-y2)**2))
        def bfs(start):
            q = deque([start]) 
            seen = {start}
            while q:
                curr = q.popleft()
                for nb in graph[curr]:
                    if nb not in seen:
                        q.append(nb)
                        seen.add(nb)
            return len(seen)

        # construct
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for k in range(len(bombs)):
                if i == k:
                    continue
                b1 = bombs[i]
                b2 = bombs[k]
                x1, y1, r1 = b1
                x2, y2,_ = b2
                if r1 >= toDist(x1, y1, x2, y2):
                    graph[i].append(k)
        
        ans = 0
        for i in range(len(bombs)):
            ans = max(ans, bfs(i))
        return ans
        
    
