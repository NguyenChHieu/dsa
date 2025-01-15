class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """
        Count the 1's and 0's in num2, then simply
        put either 1/0 to match that of num1 from 
        left to right. If exhausted, put the remaining bits
        into place.
        """

        n1 = bin(num1)[2:]
        n2 = bin(num2)[2:]
        n = max(len(n1), len(n2))
        n1 = n1.zfill(n)
        n2 = n2.zfill(n)
        ans = ""

        ones = 0
        for c in n2:
            if c == "1":
                ones += 1
        zeros = n - ones

        for i in range(n):
            if n1[i] == "0":
                if zeros > 0:
                    ans += "0"
                    zeros -= 1
                    continue
                else:
                    ans += "1" * (n-i)
                    break
            else:
                if ones > 0:
                    ans += "1"
                    ones -= 1
                    continue
                else:
                    ans += "0" * (n-i)
                    break
        return int(ans,2)
