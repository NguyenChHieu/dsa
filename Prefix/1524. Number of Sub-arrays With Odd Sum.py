class Solution:
    """
    Check the parity of the prefix sums. If encounter
    a even ps, then add #odd ps to the answer. Else
    add #even ps to the answer
    """
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = 0
        even = 1
        ans = pref = 0
        for num in arr:
            # e - e = e or o - o = e
            # e - o = o or o - e = o
            pref += num
            if pref % 2 == 0:
                even += 1
                ans += odd
            else:
                odd += 1
                ans += even
        return ans % (10**9 + 7)
            
            
        
