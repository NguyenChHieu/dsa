class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        h = []
        s = set()
        ans = 0

        for i in range(n):
            heapq.heappush(h, (nums[i], i)) # break ties

        while h:
            num = heapq.heappop(h)
            idx = num[1] 
            if idx in s:
                continue
            s.update([max(0, idx-1), idx, min(n-1,idx+1)]) # hashset keep track of marked ele
            ans += num[0]
        return ans

