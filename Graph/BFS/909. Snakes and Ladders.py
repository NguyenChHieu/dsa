class Solution:
    """
    Intuition is to figure how to flatten the board.
    Simply iterate from n**2 back to 1, and for every row
    the cols are reversed.

    No need to min() since inherently BFS will guarantee every
    path would be the smallest possible.

    Why only care about the unvisited nodes? This is because
    if nodes are already visited, that means the current path to the node
    isnt optimal due to BFS, if the node is alr visited then
    exist a shorter path to that node. Hence skip this node.
    """
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n ** 2 + 1)
        label = 1
        columns = list(range(0, n))
        for row in range(n - 1, -1, -1):
            for col in columns:
                cells[label] = (row, col)
                label += 1
            columns.reverse()  # for even rows n-1 -> 0, odd rows: 0 -> n-1

        q = deque([1])  # (label, steps)
        dist= [-1] * (n**2 + 1)
        dist[1] = 0
        while q:
            curr = q.popleft()
            for next_lb in range(curr+1, min(curr+6, n**2)+1):
                r, c = cells[next_lb] 
                dest = board[r][c] if board[r][c] != -1 else next_lb

                if dist[dest] == -1:
                    dist[dest] = dist[curr] + 1
                    q.append(dest)

        return dist[n**2]
                
