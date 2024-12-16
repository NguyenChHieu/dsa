class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        pq = [
            (-ord(k), v) for k, v in Counter(s).items()
        ] 
        heapify(pq)
        ans = []
        cnt = 0
        while pq:
            k, v = heappop(pq)
            if ans and ans[-1] == k and cnt == repeatLimit:
                # c1.1: reach limit, but no other different char to add
                if not pq:
                    break
                # c1.2: take 2nd largest char since reach limit
                kk, vv = heappop(pq)
                ans.append(kk)
                cnt = 1  # we're about to continue adding k to our ans so we set cnt to 1

                if vv - 1:
                    heappush(pq, (kk, vv - 1))
                heappush(pq, (k, v))
            else:
                # nothing in our final answer/ final answer last character != new char -> cnt = 0
                if not ans or ans[-1] != k:
                    cnt = 0
                # batch add characters
                cnt += repeatLimit
                ans.extend([k] * min(v, repeatLimit))
                # can still reuse the character -> add it to the heap
                if v - cnt > 0:
                    heappush(pq, (k, v - cnt))
        return "".join(chr(-x) for x in ans)


    # initial approach beat 22%
    # def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
    #     c = {}
    #     for ch in s:
    #         c[ch] = 1 if ch not in c else c[ch] + 1

    #     save = sorted(c.keys(), reverse=True)
    #     ans = ""
    #     curr = 0
    #     i = 0

    #     while c:
    #         if curr == repeatLimit:
    #             if len(c) <= 1:
    #                 break
    #             i += 1
    #             curr = 0
    #             ans += save[i]
    #             if c[save[i]] - 1 == 0:
    #                 del c[save[i]]
    #                 save.remove(save[i])
    #             else:
    #                 c[save[i]] -= 1
    #             i -= 1

    #         else:
    #             ans += save[i]
    #             curr += 1
    #             if c[save[i]] - 1 == 0:
    #                 del c[save[i]]
    #                 i += 1
    #                 curr = 0
    #             else:
    #                 c[save[i]] -= 1
    #     return ans


        
        
