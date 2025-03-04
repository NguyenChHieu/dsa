class Solution:
    # if r = 2 -> the sum must be 2 * 3^n -> not valid
    def checkPowersOfThree(self, n: int) -> bool:
        while n != 0:
            n,r = divmod(n, 3)
            if r > 1:
                return False
        return True

