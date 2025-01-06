class Solution:
    # def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
    #     n = len(s)
    #     st = [0] * n

    #     for shift in shifts:
    #         start = shift[0]
    #         e = shift[1]
    #         direction = shift[2]
            
    #         for i in range(start, min(e + 1, n)): # avoid exceeding length
    #             st[i] = st[i] + 1 if direction == 1 else st[i] -1
        
    #     ans = ''
    #     for i in range(len(s)):
    #         ch = s[i]
    #         newChar = ord(ch) + (st[i] % 26) # avoid shift amount exceed 26
    #         if newChar > ord('z'):
    #             newChar = ord('a') + (newChar - ord('z') - 1)
    #         elif newChar < ord('a'):
    #             newChar = ord('z') - (ord('a') - newChar - 1)
    #         ans += chr(newChar)
    #     return ans

    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        """
        Keep a prefix sum of the dates. For example: if prefix[i] = 1
        then every single number uptil ith index is incremented by 1.
        To handle the ranges, 
        
        for e.g query = [2,4,5]: we can do sth like
        prefix[2] = -1 --> all the chr uptil 2nd idx decrement by 1, prefix
        [4] --> til 4th idx all char +1. 

        Why this work? loop from end and keep a var like currentDiff - this
        will be applied to each character. The +1 , -1 will even out the currentDiff
        = 0 when the idx reached 2nd idx.

        Process - get the prefix. Loop from end - apply the currentDiff to current ch
        then update the currentDiff. Do that until finishes.
        """
        prefix_diff = [0] * (len(s) + 1)

        for shift in shifts:
            start = shift[0]
            e = shift[1]

            # handle range queries
            prefix_diff[start] += (-1 if shift[2] == 1 else 1)
            prefix_diff[e + 1] += (1 if shift[2] == 1 else -1)

        arr = [ord(c) - ord('a') for c in s]
        curr_diff = 0
        for i in reversed(range(len(prefix_diff))):
            curr_diff += prefix_diff[i]
            arr[i-1] = (arr[i-1] + curr_diff) % 26 # scale ve 0-> 25
        arr = [chr(ord("a") + n) for n in arr] # adjust ascii
        return "".join(arr)

            

