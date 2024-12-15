class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # priority = RoC = a+1/b+1 -a/b
        n = len(classes)
        classes = [(-float((c[0]+1)/(c[1]+1) - c[0]/c[1]), c) for c in classes]
        heapq.heapify(classes)

        for _ in range(extraStudents):
            c = heapq.heappop(classes)
            newC = [c[1][0] + 1, c[1][1] + 1]
            newRate = float((newC[0]+1)/(newC[1]+1) - newC[0]/newC[1])
            heapq.heappush(classes, (-newRate, newC))
        
        ans = 0
        while classes:
            cl = heapq.heappop(classes)
            c = cl[1]
            ans += float(c[0]/c[1])
        return ans/n
