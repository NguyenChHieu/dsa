class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        pr = [defaultdict(int)]
        
        for i in range(n):
            new_map = pr[-1].copy()
            new_map[s[i]] += 1
            pr.append(new_map)

        res = []
        for l, r, k in queries:
            count = defaultdict(int)
            for ch in set(pr[r + 1]) | set(pr[l]):
                count[ch] = pr[r + 1].get(ch, 0) - pr[l].get(ch, 0)
            
            odd = sum(v % 2 for v in count.values())
            res.append(odd // 2 <= k)
        return res

    # alphabet dict for each idx then perform prefix sum. 
    # def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
    #     pr = [{}]
    #     h = defaultdict(int)
    #     for i in range(len(s)):
    #         h[s[i]] += 1
    #         pr.append(h.copy())

    #     ans = [False] * len(queries)
    #     for i in range(len(queries)):
    #         l, r, k = queries[i]
    #         c = pr[r+1].copy()
    #         for key, v in pr[l].items():
    #             c[key] -= v
    #         check = True
    #         single = False
    #         for v in c.values():
    #             if v % 2 == 0:
    #                 continue
    #             if single:
    #                 if v % 2 == 1:
    #                     if k == 0:
    #                         check = False
    #                         break
    #                     k -= 1
    #                     single = False
    #                     continue
    #             single = True
    #         ans[i] = check
    #     return ans
