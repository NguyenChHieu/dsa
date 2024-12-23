class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        def search(height, mono_st):
            l = 0
            r = len(mono_st) -1
            ans = -1
            while l <= r:
                m = (l+r) // 2
                if mono_st[m][0] > height:
                    ans = max(ans,m)
                    l = m + 1
                else:
                    r = m - 1
            return ans
        
        st = [] # mono desc
        res = [-1 for _ in range(len(queries))]
        new_q = [[] for _ in range(len(heights))]

        for i in range(len(queries)):
            a = queries[i][0]
            b = queries[i][1]

            if a > b:
                a, b = b, a
            
            # handle all the cases the latter idx > former idx 
            # and latter higher than prev

            """
            Therefore any queries which makes a increasing tendency like
             /|
            /_|
            will be processed here  
            """
            if heights[b] > heights[a] or a == b:
                res[i] = b
            else:
                """ 
                - Save the query to its right building (the one with larger index) ~ b in this case
                - Tuple of
                1) Height of the left building (with height > height of right building)
                2) Index of the query (in the initial queries list)
                """
                new_q[b].append((heights[a], i))

        for i in range(len(heights) -1 , -1 ,-1):
            mono_sze = len(st)
            for a,b in new_q[i]:
                position = search(a, st)
                if 0 <= position < mono_sze: # exist a leftmost building
                    res[b] =  st[position][1]
            # preserve monotonic
            while st and st[-1][0] <= heights[i]:
                st.pop()
            st.append((heights[i],i))
        return res

        # brute force - TLE
        
        # ans = [-1] * len(queries)
        # idx = 0
        # for i in range(len(queries)):
        #     largerI = max(queries[i][0], queries[i][1])
        #     higher = max(heights[queries[i][0]], heights[queries[i][1]])

        #     if queries[i][0] == queries[i][1]:
        #         ans[idx] = queries[i][0]
        #     elif queries[i][0] < queries[i][1] and heights[queries[i][0]] < heights[queries[i][1]]:
        #         ans[idx] = queries[i][1]
        #     elif queries[i][0] > queries[i][1] and heights[queries[i][0]] > heights[queries[i][1]]:
        #         ans[idx] = queries[i][0]
        #     else:
        #         for k in range(largerI, len(heights)):
        #             if heights[k] > higher:
        #                 ans[idx] = k
        #                 break
        #     idx += 1
        # return ans
            
        
