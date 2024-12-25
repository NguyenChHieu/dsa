class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        """
        Connect node a in tree1 -> node b in tree2. Result diameter max() of 3 values:
        1) The diameter of tree 1.
        2) The diameter of tree 2.
        3) Len() longest path starts a (completely within Tree 1) + len() longest path that
        starts at node b (completely within Tree 2) + 1 (new edge between a,b).

        - 1), 2) can be observed as constants, does not change no matter which node with indeg = 0
        --> Problem of minimizing the 3).

        - It can be show that if picking the center node of the diameter of both trees, then the
        res_diam = diam1/2 + diam2/2 + 1, and it is the smallest possible val.
        """
        tree1 = self.construct(edges1, len(edges1) + 1)
        tree2 = self.construct(edges2, len(edges2) + 1)

        diam1 = self.calc_diameter(tree1)
        diam2 = self.calc_diameter(tree2)

        # ceil because when /2 the diam_res would take the bigger half, e.g 7 -> 3+4 then take 4.
        return max(diam2, diam1, ceil(diam1 / 2) + ceil(diam2 / 2) + 1)

    def calc_diameter(self, tree):
        # since using bfs, it would ensure no matter the node picked, the diameter would be the same.
        farthest_node, _ = self.bfs(tree, 0)
        _, diameter = self.bfs(tree, farthest_node)
        return diameter

    def bfs(self, tree, node):
        seen = set()
        seen.add(node)
        farthest, max_dist = node, 0
        q = deque([(node, 0)])
        while q:
            curr, dist = q.popleft()
            if dist > max_dist:
                farthest, max_dist = curr, dist

            for nb in tree[curr]:
                if nb not in seen:
                    seen.add(nb)
                    q.append((nb, dist + 1))
        return farthest, max_dist

    def construct(self, edges, size):
        graph = [[] for _ in range(size)]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        return graph