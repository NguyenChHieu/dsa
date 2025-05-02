class Solution:
    def pushDominoes(self, d: str) -> str:
        d = list(d)
        q = deque()
        for i in range(len(d)):
            if d[i] == 'L' or d[i] == 'R':
                q.append((d[i], i))

        while len(q) >= 2:
            fst, i = q.popleft()
            sec, j = q[0]
            if fst == 'R' and sec == 'L':
                for k in range(i+1, j):
                    if k - i == j - k: continue  # mid
                    elif k - i < j - k: d[k] = 'R'
                    else: d[k] = 'L'
                q.popleft()                   
            else:
                if fst == 'L':
                    for k in range(i - 1, -1, -1):
                        if d[k] != '.':
                            break
                        d[k] = 'L'
                else:
                    for k in range(i+1, len(d)):
                        if d[k] != '.':
                            break
                        d[k] = 'R' 
        if q:
            fst, i = q.popleft()
            if fst == 'L':
                for k in range(i - 1, -1, -1):
                    if d[k] != '.':
                        break
                    d[k] = 'L'
            else:
                for k in range(i + 1, len(d)):
                    if d[k] != '.':
                        break
                    d[k] = 'R'
        return ''.join(d)

        

        # prev = None
        # while q:
        #     di, idx = q.popleft()
        #     if di == 'L':
