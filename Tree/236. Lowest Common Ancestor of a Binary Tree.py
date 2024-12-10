# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 3 case with root:
        # root == p or root == q -> return p
        # p and q in differemt subtree
        # p in same subtree

        if not root:
            return None

        # c1
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p,q)
        right = self.lowestCommonAncestor(root.right, p,q)

        # c2
        if left and right:
            return root

        #c3
        return left or right