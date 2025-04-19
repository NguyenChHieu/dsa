class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            if i == headID:
                continue
            graph[manager[i]].append(i)
        
        ans = 0
        def dfs(node, time):
            nonlocal ans
            #leaf
            if not graph[node]:
                ans = max(ans, time)
                return 
            for nb in graph[node]:
                dfs(nb, time + informTime[node])
        dfs(headID, 0)
        return ans
