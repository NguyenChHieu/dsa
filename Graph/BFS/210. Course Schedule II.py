class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        indeg = [0] * numCourses
        graph = defaultdict(list)
        for v1, v2 in prerequisites:
            graph[v2].append(v1)  
            indeg[v1] += 1

        q = deque([i for i in range(numCourses) if not indeg[i]])
        ans = []
        # bfs, with indeg array to control the order
        while q:
            sj = q.popleft()
            ans.append(sj)
            for nb in graph[sj]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    q.append(nb)
        return ans if len(ans) == numCourses else []
