class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        """
        1) Find the longest cycle (closed circle)

        2) Find every compponents with len 2 cycles -> find max path in each of them
        , sum up the paths.

        ans = max( 1), 2) )
        """
        n = len(favorite)
        longest_cycle = 0
        seen = [False] * n
        cycle2_ls = []

        """
        1)
        """
        for i in range(n):
            # start will be used to find the length of the cycle 
            # (length of the traversed nodes - length of nodes until start == cur (nodes that are not in the cycle))

            # cur will be used to traverse + mark the start of the cycle
            start, cur = i, i 
            current_component = set()

            while not seen[cur]:
                seen[cur] = True # visited
                current_component.add(cur)
                cur = favorite[cur]
            
            if cur in current_component:
                cycle_length = len(current_component)
                while start != cur: # the nodes are still outside the cycle
                    cycle_length -= 1
                    start = favorite[start]
                longest_cycle = max(longest_cycle, cycle_length)

                # add length-2 cycles to ls
                if cycle_length == 2:
                    cycle2_ls.append([cur, favorite[cur]])
        """
        2)
        """
        inverted = defaultdict(list) # use a list now since the observation all node has 1 edge will be broken
        for dst, src in enumerate(favorite):
            inverted[src].append(dst)
        
        def bfs(src, parent):
            q = deque([(src, 0)])
            max_length = 0

            while q:
                node, steps = q.popleft()
                if node == parent:
                    continue

                max_length = max(max_length, steps)

                for nb in inverted[node]:
                    q.append((nb, steps+1))
            return max_length

        chained_sum = 0
        for n1,n2 in cycle2_ls:
            # longest path from n1, n2 and including both nodes itself
            chained_sum += bfs(n1, n2) + bfs(n2, n1) + 2 
        return max(chained_sum, longest_cycle)
