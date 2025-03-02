class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        fst = 0
        sec = 0
        ans = []
        while fst < len(nums1) and sec < len(nums2):
            if nums1[fst][0] == nums2[sec][0]:
                ans.append([nums1[fst][0], nums1[fst][1] + nums2[sec][1]])
                fst += 1
                sec += 1
            elif nums1[fst][0] > nums2[sec][0]:
                ans.append(nums2[sec])
                sec += 1
            else: 
                ans.append(nums1[fst])
                fst += 1

        while fst < len(nums1):
            ans.append(nums1[fst])
            fst += 1
        
        while sec < len(nums2):
            ans.append(nums2[sec])
            sec += 1
        return ans
