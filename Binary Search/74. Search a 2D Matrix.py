class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while l <= r:
            mid = (l + r) // 2
            mid_r = mid // n
            mid_c = mid % n

            if matrix[mid_r][mid_c] == target:
                return True
            elif matrix[mid_r][mid_c] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

