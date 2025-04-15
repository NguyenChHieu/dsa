class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """
        1) Map nums2 to nums1’s index space → mapped_nums2 shows how nums2 elements are positioned in nums1.
        2) As you scan mapped_nums2, you're treating each index j as the middle of a triplet.
        3) Use a SortedList to:
        Count how many earlier values (is) are less than current (left_count).
        Estimate how many later values (ks) are greater than current (right_count).
            n - curr_pos - 1:
            → Total number of values in mapped_nums2 that are greater than curr_pos, in theory.
            (Since curr_pos is an index in nums1, higher values mean a larger original index.)
            i - left_count:
            → Of the i elements before current, how many are greater than or equal to curr_pos.
            How?
            i = how many elements we've already processed (left of i)
            left_count = how many of those are < curr_pos
            So i - left_count = how many are ≥ curr_pos
        Multiply left_count * right_count to get how many triplets (i, j, k) can be formed with j as the middle.
        """
        n = len(nums1)
        pos1 = {nums1[i]: i for i in range(n)}
        nums2_relative = [pos1[num] for num in nums2]
        l_smaller = SortedList()

        ans = 0
        for i in range(n):
            curr_pos = nums2_relative[i]
            l_cnt = l_smaller.bisect_right(curr_pos)
            r_cnt = (n - curr_pos - 1) - (i - l_cnt)
            ans += l_cnt * r_cnt
            l_smaller.add(curr_pos)
        return ans
