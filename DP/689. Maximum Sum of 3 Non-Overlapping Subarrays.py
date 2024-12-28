class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
    intuition - find each distinct non-overlapping k-length subarrays
    by prefix sum. 
    Dp part: Then use memo arrays to store the best left-subarray
    to the left of the current subarray, and the best right-subarray to
    the right of the current subarray. 
    Then simply iterate through the middle subarrays and find the best
    combination of left, middle, and right subarrays.
    """
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # 1 <= k <= floor(nums.length / 3) --> always exist a valid return ans

        pref = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            pref[i] = pref[i-1] + nums[i-1]

        # precompute subarrays
        no_subarr = len(nums)-k+1
        subarr = [0] * (len(nums) -k +1)
        for i in range(no_subarr):
            subarr[i] = pref[k+i]-pref[i]
        l_max = [0] * no_subarr
        r_max = [no_subarr -1] * no_subarr
        
        # dp part
        for i in range(1, no_subarr):
            if subarr[i] > subarr[l_max[i-1]]:
                l_max[i] = i
            else:
                l_max[i] = l_max[i-1]

        for i in range(no_subarr-2, -1, -1):
            if subarr[i] >= subarr[r_max[i+1]]:
                r_max[i] = i
            else:
                r_max[i] = r_max[i+1]

        ans = []
        curr = 0
        # start from k to give space for left arr, and end at no_subarr-2k
        # to give space for right arr and middle arr itself
        for i in range(k, len(nums) - 2*k + 1):
            l = l_max[i-k]
            r = r_max[i+k]
            if subarr[l] + subarr[i] + subarr[r] > curr:
                curr = subarr[l] + subarr[i] + subarr[r]
                ans = [l, i, r]
        return ans

