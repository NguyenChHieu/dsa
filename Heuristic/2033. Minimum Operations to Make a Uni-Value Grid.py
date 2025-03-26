class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        def count(target):
            ans = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    num = grid[i][j]
                    if (target - num) % x != 0:
                        return -1
                    ans += abs(target - num) // x
            return ans

        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        nums = [num for row in grid for num in row]
        nums.sort()
        mid = len(nums) // 2
        return count(nums[mid]) if len(nums) % 2 == 0 \
            else min(count(nums[mid]), count(nums[mid-1]))
