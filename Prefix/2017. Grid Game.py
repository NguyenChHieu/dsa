class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        """
        Greedy does not work - the red robot will split the 
        cells into 3 sections - bottm left/selected cells by red/ top right
        
        Blue can only choose either top right/ bott left section -> but prefix
        takes both of them into account

        simply keep track of the max amount that red can minimize (res) so when
        comparing the bleft/topright value of new i then we can compare if 
        """
        n_grid = len(grid[0]) + 1

        pref_0 = [0] * n_grid
        pref_1 = [0] * n_grid

        for i in range(1, n_grid):
            pref_0[i] = grid[0][i - 1] + pref_0[i - 1]
            pref_1[i] = grid[1][i - 1] + pref_1[i - 1]
        
        pref_0.pop(0)
        pref_1.pop(0)

        res = float('inf') # amount that
        for i in range(n_grid-1):
            top = pref_0[-1] - pref_0[i]
            bot = pref_1[i-1] if i > 0 else 0
            blue = max(top, bot)
            res = min(blue, res)
        return res
