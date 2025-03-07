class Solution:
    # sieve of eratosthenes
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True for _ in range(right+1)]
        prime[0] = False
        prime[1] = False
        p = 2
        while p**2 <= right:
            if prime[p] == True:
                for i in range(p*p, right+1, p):
                    prime[i] =False
            p += 1

        ls = deque()
        a, b = -1, -1
        m = float('inf')
        for i in range(left, right +1):
            if prime[i]:
                ls.append(i)
                if len(ls) == 2:
                    if ls[1] - ls[0] < m:
                        m = ls[1] - ls[0]
                        a,b = ls[0],ls[1]
                elif len(ls) > 2:
                    ls.popleft()
                    if ls[1] - ls[0] < m:
                        m = ls[1] - ls[0]
                        a,b = ls[0], ls[1]
        return [a,b] if a != -1 and b != -1 else [-1,-1]
