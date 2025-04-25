class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
    # prefix of cnt (% modulo == k) until i-th idx
        pref = [0] * len(nums)
        pref[0] = 1 if nums[0] % modulo == k else 0
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] + (1 if nums[i] % modulo == k else 0)
        map = defaultdict(int)
        map[0] = 1
        ans = 0
        for i in range(len(nums)):
            target = (pref[i] - k + modulo) % modulo  # rewrite from (pref[i] - pref[j]) % modulo == k
            ans += map[target]  # found a matching pair
            map[pref[i] % modulo] += 1  # count the current pref
        return ans
