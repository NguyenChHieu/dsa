class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []

        for num in nums:
            if len(arr) < k:
                heapq.heappush(arr, num)
            else:
                # peek top ele
                if  > arr[0]:
                    heapq.heappush(arr, num)
                    heapq.heappop(arr)
        return arr[0]
