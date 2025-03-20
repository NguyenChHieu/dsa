class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        track = defaultdict(int)

        for trip in trips:
            track[trip[1]] += trip[0]
            track[trip[2]] -= trip[0]
        
        track = dict(sorted(track.items()))
        cap = 0
        for psg in track.values():
            cap += psg
            if cap > capacity:
                return False
        return True
