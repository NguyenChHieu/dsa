# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            new = TreeNode(val)
            return new
        
        prev = None
        curr = root
        # simply traverse to an external node, prev will hold the parent node of the external node
        while True: 
            prev = curr
            curr = curr.right if val > curr.val else curr.left
            if not curr:
                new = TreeNode(val)
                if prev.val < val:
                    prev.right = new
                else:
                    prev.left = new
                break
        return root
