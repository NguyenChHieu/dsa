# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.save = set()
        self.dfs(self.root, 0)

    def find(self, target: int) -> bool:
        return target in self.save
        
    def dfs(self,node, curr_val):
        if not node:
            return
        self.save.add(curr_val)
        if node.left:
            self.dfs(node.left, curr_val * 2 +1)
        if node.right:
            self.dfs(node.right,  curr_val * 2 +2)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
