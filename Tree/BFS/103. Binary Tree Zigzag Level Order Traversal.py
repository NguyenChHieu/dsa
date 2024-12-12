# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use stack-like array and alternate the order of appending the childs
        if not root:
            return []

        new_lv = [root]
        curr = 0
        ans = [[root.val]]

        while new_lv:
            next_lv = []
            lv = []
            while new_lv:
                node = new_lv.pop()
                if curr % 2 == 0:
                    if node.right:
                        next_lv.append(node.right)
                        lv.append(node.right.val)
                    if node.left:
                        next_lv.append(node.left)
                        lv.append(node.left.val)
                else:
                    if node.left:
                        next_lv.append(node.left)
                        lv.append(node.left.val)
                    if node.right:
                        next_lv.append(node.right)
                        lv.append(node.right.val)
            new_lv = next_lv
            if lv:
                ans.append(lv)
            curr += 1
        return ans
                    

