class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list) #hashmap
        for i in range(n):
            # this is an undirected graph so only 
            # visit the upper stair is sufficient
            for j in range(i+1,n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        seen = set()
        ans = 0
        # 0 -> n-1
        for i in range(n):
            if i not in seen: # new province
                seen.add(i)
                ans += 1
                dfs(i)
        return ans

