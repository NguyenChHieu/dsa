class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        """
        - Build the graph as an adj list and tracks the degrees.
        - Find all the leaf nodes (deg =1), then process them 1 by 1
        - For each node processed, decrement its deg, and check if the 
        values[curr] is divisible by k 
        --> if yes, this means all the nodes that have been processed
        until the current node makes a valid connected component --> ans += 1
        --> if no, add its value to its neighbours (only the ones with deg > 0)
        for further processing, also decrement the nb's degree
            Any neighbour that has deg == 1 now act as the next leaf node to 
            be processed.

        + sum(values) % k == 0 and edges represent a valid tree.
        --> It either form independent k-divisible components or 
        contribute their values to their parent, simplifying the 
        problem as the tree is reduced iteratively.
        """

        # edge
        if n <= 1:
            return 1 

        graph = defaultdict(list)
        deg = [0] * n # keep track of degree - approaching bottom up
        for v1,v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
            deg[v1] += 1
            deg[v2] += 1
        
        # find initial leaves
        q = deque()
        for i in range(n):
            if deg[i] == 1:
                q.append(i)

        #process the leaves, update the value along the traversal
        ans = 0
        new_vals = values[:]
        while q:
            curr = q.popleft()
            deg[curr] -= 1
            curr_val_carry = 0

            if new_vals[curr] % k == 0: # node itself is a cc
                ans += 1
            else:
                curr_val_carry = new_vals[curr] # carry to its parents' sum
            
            # update the nbr's curr_sum and degree
            for nb in graph[curr]:
                if deg[nb] == 0: # node alr processed every of its nbours 
                    continue
                deg[nb] -= 1
                new_vals[nb] += curr_val_carry
                if deg[nb] == 1:
                    q.append(nb)
        return ans
