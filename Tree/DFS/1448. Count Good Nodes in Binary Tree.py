# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # keep track of the max element along the path
        def dfs(root, maxSoFar):
            if not root:
                return 0
            
            left = dfs(root.left, max(maxSoFar, root.val))
            right = dfs(root.right, max(maxSoFar, root.val))
            return left+right+1 if root.val >= maxSoFar else left+right
        
        return dfs(root, float("-inf"))

        