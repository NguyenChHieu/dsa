class Solution:
    """
    2) construct number 
    """
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(num, length):
            if length == n:
                ans.append(num)
                return
            last_d = num % 10
            valid_ds = {last_d -k, last_d + k}

            for d in valid_ds:
                if 0<=d<10:
                    backtrack(num * 10 + d, length + 1)
        ans = []
        for i in range(1,10):
            backtrack(i, 1)
        return ans

        
    """
    1) simple array conversion
    """
    # def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
    #     def backtrack(curr):
    #         if len(curr) == n:
    #             ans.append(int("".join(curr)))
    #             return

    #         for i in range(10):
    #             if not curr:
    #                 if i == 0:
    #                     continue
    #                 backtrack(curr + [str(i)])
    #             else:
    #                 if abs(i - int(curr[-1])) == k:
    #                     backtrack(curr + [str(i)])

    #     ans = []
    #     backtrack([])
    #     return ans

    

