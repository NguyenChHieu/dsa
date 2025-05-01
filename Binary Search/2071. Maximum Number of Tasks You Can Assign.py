class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n,m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(mid):
            p = pills
            ws = SortedList(workers[m-mid:])
            for i in range(mid-1, -1, -1):
                if tasks[i] <= ws[-1]:
                    ws.pop()
                else:
                    if p == 0: # no pills
                        return False
                    weak = ws.bisect_left(tasks[i]-strength)
                    if weak == len(ws): # no worker can do it
                        return False
                    p -= 1 # some weak worker can
                    ws.pop(weak)
            return True
        
        l, r, ans = 1, min(m, n), 0
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
