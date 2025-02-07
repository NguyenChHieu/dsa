class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_map = {} # color : set of balls
        ball_map = {} # ball : curr_color
        ans = []

        for x,y in queries:
            if x in ball_map:
                old_color = ball_map[x]

                # remove the ball for color_map
                color_map[old_color].remove(x)
                if not color_map[old_color]:
                    color_map.pop(old_color)
            
            ball_map[x] = y
            if y not in color_map:
                color_map[y] = {x}
            else:
                color_map[y].add(x)

            ans.append(len(color_map))
        return ans
            
                

                
