    class Solution:
        def check(self, nums: List[int]) -> bool:
            lim = nums[0]
            rotated = False

            """ 
            if encounter a smaller number, either 
            - its a rotated sequence --> no number is greater than prevMin (the smallest num of last seq)
            - some false cases:
                + 1) exist a number greater than prevMin
                + 2) a number in new seq is < lim.
            """
            for i in range(1,len(nums)):
                # detect a possible rotated seq
                if nums[i] < lim:
                    # c2
                    if rotated:
                        return False
                    rotated = True
                    lim = nums[i]
                else:
                    lim = nums[i]

                # c1
                if rotated:
                    if nums[i] > nums[0]:
                        return False
            return True
