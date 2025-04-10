class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # calc(x) - numbers that are <= limit
        # count +1 the suffix if
            # len(x) >= s (long enough to hold s)
            # x_suffix ≥ s ⇒ the number prefix + s is ≤ x (x-prefix=x_suffix)
        # prefix part - |x| - |s| = preLen
        # for each digit 
            # -> if exceeds limit, current digit IN [0, LIMIT], and all other bits (preLen - i) - incl i-th bit, will range from [0, LIMIT]
            # = (limit + 1) * (limit + 1)^(preLen-i-1)
            # -> if not __ , current digit IN [0, x[i]] , and all other bits (preLen - i -1) will range from [0, LIMIT]
            # = (x[i] + 1) * (limit + 1)^(preLen-i-1)
        def calc(x):
            if len(x) < len(s):
                return 0
            if len(x) == len(s):
                return 1 if x >= s else 0
            
            suffix = x[len(x) - len(s) :]
            preLen = len(x) - len(s)
            cnt = 0
            for i in range(preLen):
                if int(x[i]) > limit:
                    cnt += (limit + 1) ** (preLen - i)
                    return cnt # if continues, the later combinations will > limit
                cnt += (int(x[i])) * (limit + 1) ** (preLen - i - 1)

            if suffix >= s:
                cnt += 1
            return cnt

        st = str(start -1)
        f = str(finish)
        return calc(f) - calc(st)

        
