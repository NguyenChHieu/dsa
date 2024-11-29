class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = sumcurr = 0

        for num in nums:
            sumcurr += num
            # this is the key, since sumcurr -(sumcurr-k) = k
            ans += counts[sumcurr - k]
            counts[sumcurr] += 1
        return ans