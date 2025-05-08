# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# backtrack
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node, curr, values):
            if not node:
                return
            curr += node.val
            values.append(node.val)
            if not node.left and not node.right and curr == targetSum:
                ans.append(values[:])
            else:
                dfs(node.left, curr, values) 
                dfs(node.right,curr, values) 
            values.pop()
        dfs(root, 0, [])
        return ans
