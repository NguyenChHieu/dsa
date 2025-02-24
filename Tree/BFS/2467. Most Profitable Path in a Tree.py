class Solution:
    """
    Construct the graph.
    Find the most optimal path of Bob, stored the steps via BFS.
    BFS for Alice while considering the steps of Bob's path.

    + Alice step == Bob? Split
    + _________ < Bob? Take all points
    + Else ignore (nothing changes)
    """
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        bob_steps = [float('inf')] * (len(edges) + 1)
        bob_steps[bob] = 0

        save = [-1] * (len(edges) + 1)
        save[bob] = 0
        q = deque([(bob, 0)])
        parent = {bob: None}

        while q:
            curr, steps = q.popleft()
            if curr == 0:
                while parent[curr] is not None:
                    bob_steps[curr] = save[curr]
                    curr = parent[curr]
                break
            for nb in graph[curr]:
                if save[nb] == -1:
                    parent[nb] = curr
                    save[nb] = steps + 1
                    q.append((nb, steps + 1))

        ans = float("-inf")
        seen = {0} # nodes
        ini_val = amount[0] / 2 if bob_steps[0] == 0 else amount[0]
        q = deque([(0, 0, ini_val)])  # curr, steps, val

        while q:
            curr, steps, val = q.popleft()
            if curr and len(graph[curr]) == 1:
                ans = max(ans, val)
                continue
            for nb in graph[curr]:
                new_val = val
                if nb not in seen:
                    if steps + 1 == bob_steps[nb]:
                        new_val += amount[nb] / 2
                    elif steps + 1 < bob_steps[nb]:
                        new_val += amount[nb]
                    seen.add(nb)
                    q.append((nb, steps+1, new_val))
        return int(ans)
