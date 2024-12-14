from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = 0
        ans = 0
        w = SortedList() # keep track of the min/max ele 

        for r in range(len(nums)):
            w.add(nums[r])

            while w[-1] - w[0] > 2: # update the window to match constraint
                w.remove(nums[l])
                l += 1
            ans += r-l+1 # num of possible subarr in the window
        return ans
        
