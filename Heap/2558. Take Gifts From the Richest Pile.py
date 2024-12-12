class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # heap
        gifts = [gift * -1 for gift in gifts]
        heapq.heapify(gifts)

        ans = 0
        for _ in range (k):
            heapq.heappush(gifts,int(-1 * sqrt(-1 *heapq.heappop(gifts))))
        
        return -sum(gifts)
            
