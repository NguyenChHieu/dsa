class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = []

        for _ in range(rowIndex+1):
            nr = []
            for j in range(len(dp) + 1):
                if j == 0 or j == len(dp):
                    nr.append(1)
                else:
                    nr.append(dp[j - 1] + dp[j])
            dp = nr
        return dp
