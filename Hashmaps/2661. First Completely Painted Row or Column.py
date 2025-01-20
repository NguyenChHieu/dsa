class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        mapping = {}
        r_check = [0] * m
        c_check = [0] * n

        for i in range(m):
            for j in range(n):
                mapping[mat[i][j]] = (i,j) 
        
        for i in range(m*n):
            r, c = mapping[arr[i]]
            r_check[r] += 1
            c_check[c] += 1
            
            # row full or col full
            if r_check[r] == n or c_check[c] == m:
                return i
        return -1
        
