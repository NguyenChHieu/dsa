# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        ans = [[root.val]]
        curr_lv = q

        while curr_lv:
            new_lv = deque()
            to_ans = []
            for n in curr_lv:
                if n.left:
                    to_ans.append(n.left.val)
                    new_lv.append(n.left)
                if n.right:
                    to_ans.append(n.right.val)
                    new_lv.append(n.right)
            if to_ans:
                ans.append(to_ans)
            curr_lv = new_lv
        return ans
