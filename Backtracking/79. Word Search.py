class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # TC: n.m.3^L, L = word.length (max depth), 
        # and since each node can have 3 child 
        # (from prev char, next char only have 3 possibilities.) -> 3^L nodes
        # there are m x n nodes to start with too.
        def valid(r, c):
            return 0 <= r < m and 0 <= c < n

        """
        curr_pos: cell currently processed
        seen: avoid dups
        i: pointer to the word
        """
        def backtrack(curr_pos, seen, i): 
            if i == len(word):
                return True

            for dx, dy in drs:
                nx, ny = dx + curr_pos[0], dy + curr_pos[1]
                if valid(nx, ny) and (nx, ny) not in seen:
                    if word[i] == board[nx][ny]:
                        seen.add((nx, ny))
                        if backtrack((nx, ny), seen, i + 1):
                            return True
                        seen.remove((nx,ny))

        m = len(board)
        n = len(board[0])
        drs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # search all the starting chars
        chars = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    chars.append((i, j))

        for loc in chars:
            if backtrack(loc, {loc}, 1):
                return True
        return False

            
