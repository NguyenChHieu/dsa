class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        st = []
        inc = None
        ans = 0

        for i in range(len(nums)):
            if not st:
                st.append(nums[i])
                continue

            # reset the st, no trend
            if nums[i] == st[-1]:
                ans = max(ans, len(st))
                st = [nums[i]]
                inc = None
                continue

            # assign trend
            if inc is None:
                if nums[i] > st[-1]:
                    inc = True
                elif nums[i] < st[-1]:
                    inc = False
                st.append(nums[i])

            else:
                if inc:
                    if nums[i] > st[-1]:
                        st.append(nums[i])
                    else:  # <
                        ans = max(ans, len(st))
                        st = [st[-1], nums[i]]
                        inc = False

                elif not inc:
                    if nums[i] < st[-1]:
                        st.append(nums[i])
                    else:  # >
                        ans = max(ans, len(st))
                        st = [st[-1], nums[i]] # the top of old stack is also accounted
                        inc = True
        return max(ans, len(st))

"""
hoac 2 iterations, 1 lan check inc, 1 lan check desc
"""
            
            
