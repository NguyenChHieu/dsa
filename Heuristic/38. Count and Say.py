class Solution:
    # iterative
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        st = '11'
        for j in range(3, n+1):
            new = ''
            curr = None
            cnt = 0
            for i in range(len(st)):
                if not curr:
                    curr = st[i]
                    cnt += 1
                    continue
                if st[i] == curr:
                    cnt += 1
                else:
                    new += f'{cnt}{curr}'
                    cnt = 1
                    curr = st[i]
            new += f'{cnt}{curr}'
            st = new
        return st
