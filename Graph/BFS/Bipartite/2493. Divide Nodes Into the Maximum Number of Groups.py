class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        """
        Find total of bipartite layers 
        (layers are sum of max layer can be created in each comp) 
        across every component

        How? Find all components -> run BFS while also check bipartite
        condition -> sum all the groups/ 1 componoent is not bipartite? return -1
        """
        graph = defaultdict(list)
        for e1,e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        def get_component(src):
            q = deque([src])
            comp = {src}
            while q:
                node = q.popleft()
                for nb in graph[node]:
                    if nb in comp:
                        continue
                    q.append(nb)
                    comp.add(nb)
                    # this will mark everything as visited except the src of comp
                    # thats why the for loop in main code runs.
                    visit.add(nb)  
            return comp
        
        # find most layers that a bipartite graph can have (if not bipart then return -1) 
        def biggest_group(src): 
            q = deque([(src,1)])
            dist = {src:1}

            while q:
                node, group = q.popleft()
                for nb in graph[node]:
                    if nb in dist:
                        # this means the 2nd constraint is violated (diff of edge > 1)
                        if dist[nb] not in (group-1, group+1):
                            return -1
                        continue
                    dist[nb] = group + 1
                    q.append((nb, group + 1))
            return max(dist.values())

        # FULL 
        visit = set()
        ans = 0
        for node in range(1, n+1):
            # alr act as part of some component which has been checked.
            if node in visit:
                continue
            
            visit.add(node)
            component = get_component(node)
            
            max_group_of_this_comp = 0
            # BFS from every node in the component, to find the max group that can be formed.
            for src in component:
                group_cnt = biggest_group(src)
                if group_cnt == -1:
                    return -1  # not bipartite 
                max_group_of_this_comp = max(max_group_of_this_comp, group_cnt)
            ans += max_group_of_this_comp
        return ans
