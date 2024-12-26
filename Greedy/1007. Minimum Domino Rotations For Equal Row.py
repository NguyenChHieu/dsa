class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        c = defaultdict(list)
        ans = -1
        n = len(tops)
        for i in range(n):
            c[tops[i]].append(i)
            c[bottoms[i]].append(i+n)

        potential = []
        for k,v in c.items():
            if len(v) >= n: # potential cand
                check = [False] * n
                cnt = 0
                for idx in v:
                    if not check[idx % n]:
                        check[idx % n] = True
                        cnt += 1
                    if cnt == n:
                        potential.append(v)
                        break

        if potential:
            for ls in potential:
                cnt_tops = cnt_bots =  0
                for num in ls:
                    if num >= n:
                        cnt_tops += 1
                    else:
                        cnt_bots += 1

                ans = min(max(0,n - cnt_bots), max(n - cnt_tops,0))
        return ans
            

        """
        optimal

        def check(x):
            rotations_a = rotations_b = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    rotations_a += 1
                elif bottoms[i] != x:
                    rotations_b += 1
            return min(rotations_a, rotations_b)
        
        rotations = check(tops[0])
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations
        else:
            return check(bottoms[0])
        """
