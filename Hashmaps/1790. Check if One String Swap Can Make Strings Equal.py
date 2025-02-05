class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        se1 = []
        se2 = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if len(se1) == 2: # exceed 2 diff pos
                    return False
                se1.append(s1[i])
                se2.append(s2[i])
        
        if len(se1) == 1: # cant swap
            return False
        
        if not len(se1): # 0
            return True
        
        if len(se1) == 2: # can swap
            return se1[0] == se2[1] and se1[1] == se2[0] 
        return False
