class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = {}
        for num in arr:
            c[num] = 1 if num not in c else c[num] + 1

        c = sorted(list(c.values()), reverse=True)
        n = len(arr)
        ans = 0
        i = 0
        while n > len(arr)/2:
            n -= c[i]
            ans += 1
            i += 1
        return ans

                
