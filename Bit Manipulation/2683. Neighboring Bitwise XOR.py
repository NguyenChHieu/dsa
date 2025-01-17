class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # the only thing matters is the last element of derived arr.
        start_0_last = 0
        start_1_last = 1

        for i in range(len(derived)-1):
            if derived[i] == 1:
                start_0_last = 1 if start_0_last == 0 else 0
                start_1_last = 0 if start_0_last == 1 else 1
        
        return 0 ^ start_0_last == derived[-1] or 1 ^ start_1_last == derived[-1]
            
