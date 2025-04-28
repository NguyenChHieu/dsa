class Solution:
    # if curr subarray alr < k? its subarrays guarantees to be < k
    # r-l+1 = size of subarr/ #subarrays that can be added to ans
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        curr = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr * (r - l + 1) >= k:
                curr -= nums[l]
                l += 1
            ans += r - l + 1
        return ans
