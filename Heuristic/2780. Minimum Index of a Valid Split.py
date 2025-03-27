class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        c = Counter(nums)
        dmnt = 0
        cnt = 0
        for k, v in c.items():
            if v > cnt:
                dmnt = k
                cnt = v

        size = 0  # current slice
        curr = 0  # current count
        for i in range(len(nums)):
            size += 1
            if nums[i] == dmnt:
                curr += 1
            # 1st half, 2nd half must have same dominant num
            if curr > size // 2 and cnt - curr > (len(nums) - size) // 2:
                return i
            if curr > size // 2 and cnt - curr == 1 and len(nums) - size == 1:
                return i
        return -1
