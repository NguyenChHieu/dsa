class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s = set()

        fst = 0 if A[0] != B[0] else 1
        ans = [fst]* len(A)
        s = {A[0], B[0]}

        for i in range(1,len(A)):
            curr = ans[i-1]
            if A[i] == B[i]:
                curr += 1
                ans[i] = curr
                continue
            if A[i] in s:
                curr += 1
            else:
                s.add(A[i])
            if B[i] in s:
                curr += 1
            else:
                s.add(B[i])
            ans[i] = curr
        return ans
