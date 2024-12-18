class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Use a heap to keep track value of the pairs and element indexes of the pair
        # Add (i+1, j),(i,j+1) pairs each iteration till k is met or all pairs are exhausted
        # Keep a set to avoid duplication

        h = [(nums1[0]+nums2[0],(0,0))]
        added = set()
        m = len(nums1)
        n = len(nums2)
        ans = []

        while k > 0 and h:
            _, pair = heappop(h)
            i,j = pair
            ans.append([nums1[i],nums2[j]])

            if i+1 < m and (i+1,j) not in added:
                heappush(h, (nums1[i+1]+nums2[j], (i+1,j)))
                added.add((i+1,j))
            
            if j+1 < n and (i, j+1) not in added:
                heappush(h, (nums1[i]+nums2[j+1], (i, j+1)))
                added.add((i, j+1))
            k -= 1
        return ans


