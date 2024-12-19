class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top = 0
        bottom = n-1
        right = n-1
        left = 0

        ans = []
        for i in range(n):
            ans.append([0]*n)
        
        k = 1
        while k <= n**2:
            for i in range(left, right+1):
                ans[top][i] = k
                k += 1
            top += 1

            for i in range(top, bottom+1):
                ans[i][right] = k
                k += 1
            right -= 1

            for i in range(right, left-1, -1):
                ans[bottom][i] = k
                k += 1
            bottom -= 1

            for i in range(bottom, top-1, -1):
                ans[i][left] = k
                k += 1
            left += 1
        return ans

            
