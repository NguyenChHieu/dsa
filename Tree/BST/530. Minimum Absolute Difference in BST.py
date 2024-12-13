# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []

        # preorder traversal leverageing the BST property
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        arr = []
        dfs(root)
        ans = float("inf")

        for i in range(len(arr)-1):
            ans = min(ans, abs(arr[i] - arr[i+1]))

        return ans


        
        
