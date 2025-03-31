class Solution:
    # 1st, last ele always added
    # at each time a partition selects at jth index
    # sum += arr[j] + arr[j+1] (end of prev partition and start of new partition)
    # choose k max(partition) and k min(partition)
    def putMarbles(self, weights: List[int], k: int) -> int:
        p = [weights[i] + weights[i+1] for i in range(len(weights) - 1)]
        p.sort()

        ans = 0
        for i in range(k - 1):
            ans += p[len(p) - 1 - i] - p[i]
        return ans

