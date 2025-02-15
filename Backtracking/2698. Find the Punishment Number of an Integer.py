class Solution:
    def punishmentNumber(self, n: int) -> int:
        """
        def backtrack(curr, curr_sum, target):
            if curr_sum == target:
                partitions.append(curr)
                return

            if curr_sum > target:
                return

            for j in range(3):
                backtrack(curr + [num[j]], curr_sum + num[j], target)
        """

        # backtrack to find the first VALID PARTITION via dynamic partitioning
        def backtrack(curr, i, s, target):
            if i == len(s): # partition finished
                return curr[:] if sum(curr) == target else None
            
            num = 0
            for j in range(i, len(s)):
                num = num * 10 + int(s[j])
                if num > target: # the sum alr exceed i -> skip
                    return
                res = backtrack(curr + [num], j+1, s, target)
                if res:
                    return res   

        ans = 0
        for i in range(1, n + 1):
            str_num = str(i * i)
            partition = backtrack([], 0, str_num, i)
            if partition:
                ans += i * i
        return ans
