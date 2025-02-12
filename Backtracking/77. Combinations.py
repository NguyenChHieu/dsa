class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # not permutation - similar since combinations 
        # does not consider order. So use i to avoid duplicates

        # TC O(k * n!/(n-k)!) - for loop run n times, next call run n-1 times...
        # -> n!, since tree has depth k -> (n-k)! since we only go down n-k+1 layers
        # mult by k since each copy each answer takes O(k)
        def backtrack(curr, i):
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for j in range(i, n+1):
                if j not in curr:
                    curr.append(j)
                    backtrack(curr, j)
                    curr.pop()
        ans = []
        backtrack([], 1)
        return ans

