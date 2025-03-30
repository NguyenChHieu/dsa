class Solution:
    # merge intervals
    def partitionLabels(self, s: str) -> List[int]:
        # find intervals - [1st occurence of x, last __]
        track = {}
        for i in range(len(s)):
            ch = s[i]
            if ch not in track:
                track[ch] = (i,i)
            else:
                start = track[ch][0]
                track[ch] = (start,i)
        intervals = sorted(track.values())

        # detect partitions
        cuts = []
        r = intervals[0][1]
        for s, e in intervals[1:]:
            if s > r:
                cuts.append(s)
                r = e
                continue
            r = max(e, r)
        cuts.append(r + 1)

        ans = []
        curr = 0
        for cut in cuts:
            ans.append(cut - curr)
            curr = cut
        return ans
