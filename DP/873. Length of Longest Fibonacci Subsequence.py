class Solution:
    # dp(i,j) = length of the longest Fib subsq from idx i->j
    # arr[k] + arr[i] = arr[j]  
    # dp(i,j) = dp(k,i) + 1

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        idxMap = {num:i for i,num in enumerate(arr)}
        dp = defaultdict(lambda: 2)
        ans = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                length = 2
                prev = arr[j] - arr[i]
                if prev in idxMap and idxMap[prev] < i:
                    length = dp[(idxMap[prev], i)] + 1
                dp[(i,j)] = length
                ans = max(ans, length)
        return ans if ans > 2 else 0

    # TOP DOWN
    # def lenLongestFibSubseq(self, arr: List[int]) -> int:
    #     def dp(i,j):
    #         if (i,j) in memo:
    #             return memo[(i,j)]
    #         ans = 2
    #         prev = arr[j] - arr[i]
    #         # arr[k] must be before arr[i]
    #         if prev in idxMap and idxMap[prev] < i:
    #             ans = dp(idxMap[prev], i) + 1
    #         memo[(i,j)] = ans
    #         return ans

    #     memo = {}
    #     idxMap = {}
    #     M = 0
    #     for i, num in enumerate(arr):
    #         idxMap[num] = i
    #     for i in range(len(arr)):
    #         for j in range(i+1, len(arr)):
    #             M = max(M, dp(i,j))
    #     return M if M >=3 else 0

        
