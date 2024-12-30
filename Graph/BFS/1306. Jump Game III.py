class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def valid(idx):
            return 0 <= idx < len(arr)
        
        q = deque([start])
        seen = {start}

        while q:
            curr = q.popleft()
            if arr[curr] == 0:
                return True

            l = curr + arr[curr]
            r = curr - arr[curr]
            if valid(r) and r not in seen:
                q.append(r)
                seen.add(r)
            if valid(l) and l not in seen:
                q.append(l)
                seen.add(l)
        return False
