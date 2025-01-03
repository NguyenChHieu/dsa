# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        lv = 0

        while q:
            s = len(q)
            prev = float('-inf') if lv % 2 == 0 else float('inf')
            for i in range(s):
                # even lv - odd int, inc
                node = q.popleft()
                if lv % 2 == 0:
                    if node.val % 2 == 0 or node.val <= prev:
                        return False
                # odd lv - even int, inc
                else:
                    if node.val % 2 == 1 or node.val >= prev:
                        return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                prev = node.val
            lv += 1
        return True


        
