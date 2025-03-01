class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        # Graph is valid, no /0 or no contradiction
        + Each variable = a vertex
        + Equations ~ weighted edge.
        """
        def get_node_map(node):
            nonlocal node_counter
            if node not in node_map:
                node_map[node] = node_counter
                node_counter += 1
            return node_map[node]

        def bfs(st, end):
            q = deque([(st,1)])
            seen = {st}
            while q:
                curr, val = q.popleft()
                if curr == end:
                    return val
                for nb in graph[curr]:
                    mult = relation[f'{curr}->{nb}']
                    if nb not in seen:
                        seen.add(nb)
                        q.append((nb, val * mult))
            return -1

        relation = {}
        graph = defaultdict(list)
        node_map = {}
        node_counter = 0

        for i in range(len(equations)):
            node1 = get_node_map(equations[i][0])
            node2 = get_node_map(equations[i][1])
            graph[node1].append(node2)
            graph[node2].append(node1)
            relation[f'{node1}->{node2}'] = values[i]
            relation[f'{node2}->{node1}'] = 1 / values[i]

        ans = [-1] * len(queries)
        for i in range(len(queries)):
            if queries[i][0] in node_map \
                    and queries[i][1] in node_map:
                ans[i] = bfs(node_map[queries[i][0]], node_map[queries[i][1]])
        return ans


### LCODE APPROACH
def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    def answer_query(start, end):
        # no info on this node
        if start not in graph:
            return -1
        
        seen = {start}
        stack = [(start, 1)]
        
        while stack:
            node, ratio = stack.pop()
            if node == end:
                return ratio
            
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append((neighbor, ratio * graph[node][neighbor]))

        return -1
    
    graph = defaultdict(dict) # instead of convert chars to be able to use list, we use dict to keep track the mapping.
    for i in range(len(equations)):
        numerator, denominator = equations[i]
        val = values[i]
        graph[numerator][denominator] = val
        graph[denominator][numerator] = 1 / val
    
    ans = []
    for numerator, denominator in queries:
        ans.append(answer_query(numerator, denominator))
    
    return ans