# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # keep track of cur_max and curmin since when the node is null (external node)
        # then all the max/min values have been checked and updated correspondingly
        # along the way. So the max diff will be calculated correctly
        
        # the values wouldnt be mixed up with different subtrees since the curmax/min
        # will only be updated when traverse down the tree - if different subtree then its
        # in a different recursive branch.
        def dfs(node, cur_max, cur_min):
            if not node:
                return cur_max-cur_min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            
            left = dfs(node.left, cur_max, cur_min)
            right = dfs(node.right, cur_max, cur_min)
            
            return max(left, right)
        return dfs(root, root.val, root.val)