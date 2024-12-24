# class Solution:
#     def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
#         """
#         Connect node a in tree1 -> node b in tree2. Result diameter max() of 3 values:
#         1) The diameter of tree 1.
#         2) The diameter of tree 2.
#         3) Len() longest path starts a (completely within Tree 1) + len() longest path that
#         starts at node b (completely within Tree 2) + 1 (new edge between a,b).

#         - 1), 2) can be observed as constants, does not change no matter which node with indeg = 0
#         --> Problem of minimizing the 3).

#         - It can be show that if picking the center node of the diameter of both trees, then the
#         res_diam = diam1/2 + diam2/2 + 1, and it is the smallest possible val.
#         """

#         if not edges1 and not edges2:
#             return 0  # Both trees are empty
#         if not edges1:
#             return self.calc_diameter(self.construct(edges2))  # Only Tree 2 exists
#         if not edges2:
#             return self.calc_diameter(self.construct(edges1))

#         tree1 = self.construct(edges1)
#         tree2 = self.construct(edges2)

#         diam1 = self.calc_diameter(tree1)

#         diam2 = self.calc_diameter(tree2)

#         # ceil because when /2 the diam_res would take the bigger half, e.g 7 -> 3+4 then take 4.
#         return max(diam2, diam1, ceil(diam1 / 2) + ceil(diam2 / 2) + 1)

#     def calc_diameter(self, tree):
#         if not tree:
#             return 0
#         # since using bfs, it would ensure no matter the node picked, the diameter would be the same.
#         any_node = next(iter(tree))
#         farthest_node, _ = self.bfs(tree, any_node)

#         _, diameter = self.bfs(tree, farthest_node)
#         return diameter

#     def bfs(self, tree, node):
#         seen = set()
#         seen.add(node)
#         farthest, max_dist = node, 0
#         q = deque([(node, 0)])
#         while q:
#             curr, dist = q.popleft()
#             if dist > max_dist:
#                 farthest, max_dist = curr, dist

#             for nb in tree[curr]:
#                 if nb not in seen:
#                     seen.add(nb)
#                     q.append((nb, dist + 1))
#         return farthest, max_dist

#     def construct(self, edges):
#         graph = defaultdict(list)
#         for v1, v2 in edges:
#             graph[v1].append(v2)
#             graph[v2].append(v1)
#         return graph

class Solution:
    def minimumDiameterAfterMerge(self, edges1, edges2):
        # Calculate the number of nodes for each tree
        n = len(edges1) + 1
        m = len(edges2) + 1

        # Build adjacency lists for both trees
        adj_list1 = self.build_adj_list(n, edges1)
        adj_list2 = self.build_adj_list(m, edges2)

        # Calculate the diameters of both trees
        diameter1 = self.find_diameter(n, adj_list1)
        diameter2 = self.find_diameter(m, adj_list2)

        # Calculate the longest path that spans across both trees
        combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        # Return the maximum of the three possibilities
        return max(diameter1, diameter2, combined_diameter)

    def build_adj_list(self, size, edges):
        adj_list = [[] for _ in range(size)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list

    def find_diameter(self, n, adj_list):
        # First BFS to find the farthest node from an arbitrary node (e.g., 0)
        farthest_node, _ = self.find_farthest_node(n, adj_list, 0)

        # Second BFS to find the diameter starting from the farthest node
        _, diameter = self.find_farthest_node(n, adj_list, farthest_node)
        return diameter

    def find_farthest_node(self, n, adj_list, source_node):
        queue = deque([source_node])
        visited = [False] * n
        visited[source_node] = True

        maximum_distance = 0
        farthest_node = source_node

        while queue:
            for _ in range(len(queue)):
                current_node = queue.popleft()
                farthest_node = current_node

                for neighbor in adj_list[current_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

            if queue:
                maximum_distance += 1

        return farthest_node, maximum_distance
