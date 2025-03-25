class Solution:
    # since rect does not overlap, as long as the 
    # boundary by x (or by y) does not intersect,
    # it must fit in the slice

    # track gap_count, when r <= s.
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        by_x = []
        by_y = []
        for x1, y1, x2, y2 in rectangles:
            by_x.append((x1,x2))
            by_y.append((y1,y2))
        
        by_x.sort()
        by_y.sort()

        def can_cut(intervals):
            r = intervals[0][1]
            gap_count = 0
            for s,e in intervals[1:]:
                if r <= s:
                    gap_count += 1
                r = max(r, e)
            return gap_count >= 2
        return can_cut(by_x) or can_cut(by_y)
