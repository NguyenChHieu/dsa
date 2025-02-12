class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        save = defaultdict(SortedSet)

        for i in range(len(nums)):
            str_num = str(nums[i])
            cur_sum = 0
            for digit in str_num:
                cur_sum += int(digit)
            save[cur_sum].add((nums[i], i))

        ans = -1
        for k in save:
            sum_set = save[k]
            if len(sum_set) >= 2:
                ans = max(ans, sum_set[-1][0] + sum_set[len(sum_set) - 2][0])
        return ans
