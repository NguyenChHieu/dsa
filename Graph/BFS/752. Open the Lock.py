class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # consider each lock state as a node. any
        # node with diff = 1 are neighbours

        # then simply bfs through every possible
        # changes through each step. keep track 
        # of visited nodes.
        def nbours(string):
            ans = []
            for i in range(4):
                digit = int(string[i])
                for change in [1,-1]:
                    num = (digit+change) % 10
                    ans.append(string[:i] + str(num) + string[i+1:])
            return ans
        
        if '0000' in deadends:
            return -1

        q = deque([(0, '0000')])
        seen = set(deadends)
        seen.add('0000')

        while q:
            steps, state = q.popleft()
            if state == target:
                return steps # guarantee to be smallest
                # due to the attr of BFS

            for nb in nbours(state):
                if nb not in seen:
                    seen.add(nb)
                    q.append((steps +1, nb))

        return -1
