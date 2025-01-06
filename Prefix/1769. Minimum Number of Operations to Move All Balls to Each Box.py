class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls= set()
        for i in range (len(boxes)):
            if boxes[i] == '1':
                balls.add(i)
        
        ans = [0] * len(boxes)
        for i in range(len(boxes)):
            curr = 0
            for k in balls:
                if boxes[i] == 0:
                    curr += abs(i-k)
                else:
                    if i != k:
                        curr += abs(i-k)
            ans[i] = curr
        return ans
