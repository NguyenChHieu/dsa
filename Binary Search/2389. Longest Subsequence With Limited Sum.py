class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # maximum size subseq --> try to put in as much numbers as possible
        # hence the way to choose the subsequence (permutation) would be choosing the smallest numbers
        # e.g 1,2,3,4 -> size 1 -> 1, size 2 -> 1,2, size 3-> 1,2,3....
        # --> prefix sum + bs with dups(find rightmost idx)

        # find rightmost idx because the bigger the idx = the bigger the subsequence,
        # and im trying tro find the biggest subsequence that meet the conds
        
        def bs(arr, target):
            l = 0
            r = len(arr)
            while l < r:
                mid = (l+r)//2
                if arr[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        nums = sorted(nums)
        prefix = nums.copy()
        for i in range(1,len(nums)):
            prefix[i] = prefix[i] + prefix[i-1]
        
        ans = [0] * len(queries)
        
        for i in range(len(queries)):
            val = queries[i]
            ans[i] = bs(prefix, val)
        return ans
        
