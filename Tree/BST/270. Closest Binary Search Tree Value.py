# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        diff = float("inf")
        ans = []
        curr = root
        
        # traverse until reach an external node.
        while curr:
            if abs(curr.val-target) <= diff:
                # allow ties
                if abs(curr.val-target) == diff:
                    ans.append(curr.val)
                else:
                    ans.clear()
                    ans.append(curr.val)
                diff = abs(curr.val-target) 
            curr = curr.left if curr.val > target else curr.right
        return min(ans)
