class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def bfs(src, dst):
            q = deque([src])
            seen = set()
            while q:
                node = q.popleft()
                if node == dst:
                    return True
                for nb in graph[node]:
                    if nb not in seen:
                        seen.add(nb)
                        q.append(nb)
            return False
        
        graph = defaultdict(list)
        for n1,n2 in prerequisites:
            graph[n1].append(n2)

        ans = [False] * len(queries)
        for i in range(len(queries)):
            src, dst = queries[i]
            ans[i] = bfs(src, dst)
        return ans


        
