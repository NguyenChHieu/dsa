class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        # if the array is sorted, it would create n(n+1)/2 value for each ele with n = curr_index
        # 0,1,2,3,4 -> 0,1,3,6,10
        # for any index that has the matched prefix sum -> we can mark it as a chunk since its alr sorted
        # any element's index that matches that in the sorted order can be treated as a single chunk

        # ans = 0
        # curr = 0

        # for i in range(len(arr)):
        #     curr += arr[i]
        #     if curr == i*(i+1)/2:
        #         ans += 1
        # return ans

        # or simply compare current index with the "supposed-to-be" index in the sorted order
        # this is correct since the array is the permutation range: [0,n-1] 
        ans = 0
        sorted_i = 0

        for i in range(len(arr)):
            # keeping the largest index found since if a bigger element in the upperhalf appears in the lowerhalf,
            # entire (or almost) chunk would have a size > n/2 inorder to rearrange the element correctly
            sorted_i = max(sorted_i, arr[i])
            if i == sorted_i:
                ans += 1
        return ans
