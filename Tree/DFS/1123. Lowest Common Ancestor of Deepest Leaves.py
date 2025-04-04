# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = valzx x
#         self.left = left
#         self.right = right

"""
    1
   / \
  2   3
 /     \
4       5
"""

# appro - find deepest nodes, track by maxdepth
# check lca correspondingly - if depth = deepest depth + no child -> leaf
# if left and right -> found a LCA
# if left or right -> pass the child up to check for possible LCA.
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def maxDepth(node):
            if not node:
                return 0
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            return max(left, right) + 1
        def lca(node, d, deepest):
            if not node:
                return 
            # dont return early since we need to check for
            # every deepest node
            left = lca(node.left, d+1, deepest)
            right = lca(node.right, d+1, deepest)
            # leaf
            if d == deepest and not left and not right:
                return node
            # found a lca
            if left and right:
                return node
            # pass the deepest node up until reach a 
            # (possibly) a valid lca
            return left or right 
                
        
        if not root.left and not root.right:
            return root
        
        mHeight = maxDepth(root) - 1
        return lca(root, 0, mHeight)
