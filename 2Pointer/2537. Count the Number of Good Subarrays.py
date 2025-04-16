class Solution:
    """
    [3,1,4,3,2,2,4] --> window process the [3,1,4,3,2,2] --> satisfied, ans += n - r + 1
    then tries to make the window smaller -> [1,4,3,2,2] --> not sattisfied -> keep adding
    new elements to window to check (then process repeat)
    """
    def countGood(self, nums: List[int], k: int) -> int:
        ans = 0
        cur_pair = 0
        save = defaultdict(int)
        l = r = 0
        n = len(nums)
        while r < n:
            # add to window + calc pairs
            while r < n and cur_pair < k:
                save[nums[r]] += 1
                cnt = save[nums[r]]
                if cnt > 1:
                    cur_pair += cnt - 1
                r += 1
            if cur_pair >= k:
                ans += n - r + 1
            # minimize window if valid
            while l < r and cur_pair >= k:
                cur_pair -= save[nums[l]] - 1
                save[nums[l]] -= 1
                if cur_pair >= k:
                    ans += n - r + 1
                l += 1
        return ans
