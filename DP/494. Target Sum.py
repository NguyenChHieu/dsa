class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # backtracking + memo - check any leaf node in recur tree with val == target
        """
        dp = {}

        def backtrack(i, curr):
            if (i, curr) in dp:
                return dp[(i,curr)]

            if i == len(nums):
                return 1 if curr == target else 0
            
            dp[(i,curr)] = (
                backtrack(i+1, curr + nums[i]) +
                backtrack(i+1, curr - nums[i])
            ) 
            return dp[(i,curr)]
        return backtrack(0,0)
        """

        # dp - tabulation

        """
        Row = how many numbers have we used, col = current sum
        dp[r][c] = number of ways that form the curr_sum "r" and
        taken c numbers.
        dp[0][0] = 1 ~ 1 way to form curr_sum = 0 with 0 numbers.
        """
        # dp = [defaultdict(int) for i in range(len(nums)+1)]
        # dp[0][0] =1
        # for i in range(len(nums)):
        #     for curr_sum, cnt in dp[i].items():
        #         dp[i+1][curr_sum + nums[i]] += cnt
        #         dp[i+1][curr_sum - nums[i]] += cnt
        # return dp[len(nums)][target]

        # optimal - dp with only partial table - use only prev row and curr row
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(len(nums)):
            nxt_dp = defaultdict(int)
            for curr_sum, cnt in dp.items():
                nxt_dp[curr_sum + nums[i]] += cnt
                nxt_dp[curr_sum - nums[i]] += cnt
            dp = nxt_dp
        return dp[target] 

    
