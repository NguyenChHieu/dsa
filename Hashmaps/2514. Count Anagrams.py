class Solution:
    def countAnagrams(self, s: str) -> int:
        def fact(num):
            res = 1
            for i in range(2, num + 1):
                res = (res * i) % mod
            return res
        mod = 10 ** 9 + 7
        groups = s.split(' ')
        ans = 1
        for g in groups:
            c = Counter(g)
            dups = 1
            for v in c.values():
                if v >= 2:
                    dups = (dups * fact(v)) % mod
            # print(((((fact(len(g)) % mod) / dups) % mod)) % mod) # inverse modulo
            ans = (ans * (fact(len(g)) * pow(dups,-1,mod))) % mod
        return ans
