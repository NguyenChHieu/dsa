class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        st = []

        if len(s) % 2 == 1:
            return False

        # 678, make the unlocked parentheses as *, its just
        # that the number of * (represented by right_unmatched_cnt)
        # must be even in order to be flattened out the parentheses
        # eg, 4 unlocked can be arranged (())
        # in other words, there always exists a way to make an even 
        # length string of * valid.

        left_min = 0 # minimum cnt of ( unmatched
        left_max = 0 # max ____

        for i in range(len(s)):
            if locked[i] == "0":
                left_min -= 1
                left_max += 1
            else:
                if s[i] == '(':
                    left_min += 1
                    left_max += 1
                else:
                    left_min -= 1
                    left_max -= 1
            
            if left_max < 0:
                return False # no more ( left but encounter )
            if left_min < 0:
                left_min = 0 # unlocked char treated as *
        
        return (left_max % 2 == 0) and left_min == 0


            


