# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    If there are multiple layers with the same max value 
    then the algo always find the smallest level x without
    handling it, beacause BFS is approaching top down 
    """
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = lv = 0
        currMax = float('-inf')
        q = deque([root])

        while q:
            s = len(q)
            sUm = 0
            for i in range(s):
                node = q.popleft()
                sUm += node.val
                if node.left:
