class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        ans = 0
        for k,v in c.items():
            # C(k+1, k) = k+1 - max combinations for group k, if exceeds = add 1 more group + current rabbit
            # (#rabbit in that group + current rabbit) * number of groups to satisfied #rabbits replied similarly 
            ans += v if not k else (k+1) * ceil(v / (k+1)) 
        return ans

            

