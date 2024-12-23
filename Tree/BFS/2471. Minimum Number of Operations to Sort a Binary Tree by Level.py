# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # normal bfs + algo min swap (using cycles)
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def countMinSwap(arr):
            n = len(arr)
            arr_pos = [*enumerate(arr)] # (0, val1), (1, val2),...
            # true pos - sort by their values to get their sorted pos
            arr_pos.sort(key = lambda it:it[1])

            # hashmap to keep track of the nodes'visits
            hm = {k: False for k in range(n)}

            ans = 0
            for i in range(n):
                # already visited / alr at correct index
                if hm[i] or i == arr_pos[i][0]:
                    continue
                
                cycle_size = 0
                idx = i
                
                # curr node is not checked yet
                while not hm[idx]:
                    hm[idx] = True

                    cycle_size += 1
                    idx = arr_pos[idx][0] # get the sorted value at that idx
                
                if cycle_size > 0:
                    ans += cycle_size -1 
            return ans

        ans = 0
        q = deque([root]) 
        old_vals = [root.val]

        while q:
            # count here
            ans += countMinSwap(old_vals)

            new_lv = deque()
            vals = []
            for node in q:
                if node.left:
                    new_lv.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    new_lv.append(node.right)
                    vals.append(node.right.val)
            old_vals =vals
            q = new_lv
        return ans



# def minimumOperations(self, root: Optional[TreeNode]) -> int:
#         q = deque([root])
#         ans = 0
#         while q:
#             a = []
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 a.append(node.val)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             n = len(a)
#             a = sorted(range(n), key = lambda i: a[i])

#             vis = [False] * n
#             ans += n
#             for v in a:
#                 if vis[v]:
#                     continue
#                 while not vis[v]:
#                     vis[v] = True
#                     v = a[v]
#                 ans -= 1
#         return ans
