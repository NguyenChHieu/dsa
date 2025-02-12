class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(path):
            if path[-1] == len(graph)-1:
                ans.append(path[:])
                return
            for nb in graph[path[-1]]:
                # no "seen" since this is a DAG 
                # no need to pop after
                backtrack(path + [nb])
        ans = []
        backtrack([0])
        return ans
