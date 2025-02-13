class Solution:
    def minOperations(self, h: List[int], k: int) -> int:
        heapify(h)
        ans = 0
        while h[0] < k and len(h) > 1:
            fst = heappop(h)
            sec = heappop(h)

            newNum = min(fst, sec) * 2 +  max(fst, sec)
            heappush(h, newNum)

            ans += 1
        return ans

