class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        greater = []
        ans = []
        eq = 0

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                eq += 1
        
        for num in smaller:
            ans.append(num)
        for _ in range(eq):
            ans.append(pivot)
        for num in greater:
            ans.append(num)
        return ans
