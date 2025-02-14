class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]
        self.rmost_0_idx = -1 # track the rmost 0 (every product k > rmost_0_idx = 0)
        self.total = 0 # actual index

    def add(self, num: int) -> None:
        self.total += 1
        if num != 0:
            self.prefix.append(self.prefix[-1] * num)
        else:
            self.rmost_0_idx = self.total
            self.prefix = [1]            

    def getProduct(self, k: int) -> int:
        if self.total - k + 1 <= self.rmost_0_idx: 
            return 0
        return self.prefix[-1] // self.prefix[len(self.prefix) - 1 - k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
