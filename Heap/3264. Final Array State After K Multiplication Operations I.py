class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        numArr = [(nums[i],i) for i in range(len(nums))]
        heapq.heapify(numArr)
        for _ in range(k):
            num = heapq.heappop(numArr)
            # scale the target
            idx = num[1]
            nums[idx] = num[0] * multiplier
            heapq.heappush(numArr, (num[0] * multiplier, idx))

        return nums
