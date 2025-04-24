class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # k = len(set(nums))
        # hm = defaultdict(int)
        # ans = 0
        # n = len(nums)
        # for r in range(n):
        #     hm[nums[r]] += 1
        #     if len(hm) == k:
        #         ans += 1
        #         new_hm = hm.copy()
        #         for l in range(r):
        #             new_hm[nums[l]] -= 1
        #             if not new_hm[nums[l]]:
        #                 break
        #             if len(new_hm) == k:
        #                 ans += 1
        # return ans
        total_unique = len(set(nums))
        count = 0
        left = 0
        freq = {}

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            while len(freq) == total_unique:
                count += len(nums) - right 
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]] 
                left += 1

        return count
