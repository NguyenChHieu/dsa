class MedianFinder:
    # two heap approach - 
        # 1 min heap store upper branch 
        # 1 max heap store lower branch
    # if even size: pop both heap and take avg
    # if odd: pop from the heap that has more ele

    # choose 1 heap to push (and has 1 more ele if odd size) - this case choose max heap
    # now len(mx) - len(mn) <= 1
    def __init__(self):
        self.mn = []
        self.mx = []
        
    # why? 
    # max heap chosen as the one to be pushed
    # then pop from the max heap to retrieve the NEW max from the smaller half
    # push to the min heap (upper half) - if min heap has 1 more ele then pop it
    # and push it back to the max heap (since we choose it from the start) to
    # find the new top of the max heap.
    def addNum(self, num: int) -> None:
        heappush(self.mx, -num) # neg to mimic max heap
        heappush(self.mn, -heappop(self.mx))
        if (len(self.mn) - len(self.mx) == 1):
            heappush(self.mx, -heappop(self.mn))

    def findMedian(self) -> float:
        return -self.mx[0] if (len(self.mx) + len(self.mn)) % 2 == 1 else (self.mn[0]+-self.mx[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
