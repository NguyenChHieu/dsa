from typing import List
from collections import defaultdict


def maxSubarrayLength(nums: List[int], k: int) -> int:
    r = 0
    l = 0
    n = len(nums)
    save = defaultdict(int)
    ans = 0

    while r < n and n > r >= l:
        save[nums[r]] += 1
        while save[nums[r]] > k:
            save[nums[l]] -= 1
            l += 1
        ans = max(ans, r - l + 1)
        r += 1

    return ans


print(maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2))
