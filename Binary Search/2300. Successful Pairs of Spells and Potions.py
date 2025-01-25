class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        def bs(potions, spell, success):
            l = 0
            r = len(potions) - 1
            while l <= r:
                mid = (l + r) // 2
                val = spell * potions[mid]
                if val < success:
                    l = mid + 1
                else:
                    r = mid - 1
            return len(potions) - l # l will be the leftmost idx of the smallest success val 

        ans = [0] * len(spells)
        for i in range(len(spells)):
            ans[i] = bs(potions, spells[i], success)
        return ans

            

        
