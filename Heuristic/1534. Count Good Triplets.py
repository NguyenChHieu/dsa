class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        n = len(arr)
        end = n-3+1
        for i in range(end):
            for j in range(i+1, end+1):
                for k in range(j+1, end+2):
                    if abs(arr[i] - arr[j]) <= a and \
                       abs(arr[j] - arr[k]) <= b and \
                       abs(arr[i] - arr[k]) <= c:
                       ans += 1
        return ans

                
