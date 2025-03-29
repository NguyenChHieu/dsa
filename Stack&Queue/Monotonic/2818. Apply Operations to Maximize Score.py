class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int: 
        def p_score(n):
            cnt = 0
            for i in range(2, int(sqrt(n) + 1)):
                if n % i == 0:
                    cnt += 1
                    while n % i == 0:
                        n //= i
            if n >= 2:
                cnt += 1
            return cnt
        
        N = len(nums)
        score = 1
        mod = 10 ** 9 + 7

        prime_scores = [p_score(num) for num in nums]
        left_bound = [-1] * N
        right_bound = [N] * N
        st = [] # mono desc
        for i, s in enumerate(prime_scores):
            while st and prime_scores[st[-1]] < s:
                # top of stack found right bound
                idx = st.pop()
                right_bound[idx] = i
            # left bound
            if st:
                left_bound[i] = st[-1]
            st.append(i)
        
        heap = [(-n, i) for i, n in enumerate(nums)] # val, idx
        heapify(heap)
        ans = 1
        while k > 0:
            v, i = heappop(heap)
            v = -v

            left_cnt = i - left_bound[i]
            right_cnt = right_bound[i] - i
            cnt = left_cnt * right_cnt

            ops = min(cnt, k)
            ans = (ans * pow(v, ops, mod)) % mod
            k -= ops
        return ans
