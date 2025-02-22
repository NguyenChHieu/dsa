# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def converter():
            i = 0
            while i < len(traversal):
                cnt = 0
                while i < len(traversal) and traversal[i] == '-':
                    cnt += 1
                    i += 1

                num_start = i
                while i < len(traversal) and traversal[i].isdigit():
                    i += 1

                val = int(traversal[num_start:i])
                save.append((val, cnt))

        save = []
        converter()
        root = TreeNode(save[0][0])
        stack = [(root, 0)]
        for val, depth in save[1:]:
            node = TreeNode(val)
            # processed node is above current node
            while stack and stack[-1][1] >= depth: 
                stack.pop()
            if stack[-1][0].left is None:
                stack[-1][0].left = node
            else:
                stack[-1][0].right = node
            stack.append((node, depth))
        return root
        
