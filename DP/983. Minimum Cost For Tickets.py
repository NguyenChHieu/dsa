class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        # def dfs(i,curr_cost,max_day):
        #     nonlocal ans
        #     if i == len(days):
        #         ans = min(ans, curr_cost)
        #         return
        #     if days[i] < max_day:
        #         dfs(i+1,curr_cost,max_day)
        #     dfs(i+1,curr_cost+save[0][1],max_day+save[0][0])
        #     dfs(i+1,curr_cost+save[1][1],max_day+save[1][0])
        #     dfs(i+1,curr_cost+save[2][1],max_day+save[2][0])

        # ans = float('inf')
        # save = [(1,costs[0]),(7, costs[1]),(30, costs[2])]
        # dfs(0,0,0)
        # return ans

        dp = {len(days): 0}
        def dfs(i):
            if i in dp:
                return dp[i]
            dp[i] = float('inf')
            j = i 
            for cost, duration in zip(costs, [1,7,30]):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                # recursively checking all possible branches
                dp[i] = min(dp[i], cost + dfs(j)) 
            return dp[i]
        return dfs(0)
