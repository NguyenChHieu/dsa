class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # compare the cur_max(max benefit tracked til i-th idx) with the i-1th element
        # and update cur_max
        cur_max = 0
        ans =0
        
        for i in range(1, len(values)):
            # cur_max - 1 since the dist increment by 1
            cur_max = max(cur_max-1, values[i-1]-1)
            ans = max(values[i] + cur_max, ans)
        return ans
