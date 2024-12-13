# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, miN, maX):
            if not node:
                return True

            # current node must be > maxVal in left subtree
            # and < minVal in right subtree
            if miN >= node.val or node.val >= maX:
                return False
            
            left = dfs(node.left, miN, node.val)
            right = dfs(node.right, node.val, maX)

            return left and right
        
        return dfs(root, float("-inf"), float("inf"))

            
