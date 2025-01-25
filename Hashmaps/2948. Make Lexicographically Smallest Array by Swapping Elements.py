class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # if a can swapped with b, b can swapped with c -> a can be swapped with c

        s_nums = sorted(nums)

        curr_group = 0
        num_to_group = {}  # number : group_Idx
        group_to_ls = {}  # group_idx : group

        num_to_group[s_nums[0]] = curr_group
        group_to_ls[curr_group] = deque([s_nums[0]])

        for i in range(1, len(nums)):
            if s_nums[i] - s_nums[i - 1] > limit:
                curr_group += 1  # this new number has diff > limit -> belongs to new group

            num_to_group[s_nums[i]] = curr_group

            if curr_group not in group_to_ls:
                group_to_ls[curr_group] = deque([s_nums[i]])
            else:
                group_to_ls[curr_group].append(s_nums[i])

        for i in range(len(nums)):
            curr_group_idx = num_to_group[nums[i]]
            curr_group_ls = group_to_ls[curr_group_idx]

            # this would be correct since each group is partitioned after sorted (s_nums)
            # To make lexi smallest -> just make each number in nums be positioned
            # in the order of the sorted groups.
            nums[i] = curr_group_ls.popleft()  
            group_to_ls[curr_group_idx] = curr_group_ls
        return nums

        
            
