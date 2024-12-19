# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # construct a graph from a tree + find the target node (source)
        # perform bfs to find the targetted layer
        source = None
        parent = {}
        def dfs(node):
            nonlocal source
            if not node:
                return
            if node == target:
                source = node

            if node.left:
                parent[node.left]= node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)
        
        dfs(root)
        curr_lv = [source]
        seen = {source}
        while k > 0:
            new_lv = []
            for curr in curr_lv:
                seen.add(curr)
                if curr in parent and parent[curr] not in seen:
                    new_lv.append(parent[curr])
                if curr.left and curr.left not in seen:
                    new_lv.append(curr.left)
                if curr.right and curr.right not in seen:
                    new_lv.append(curr.right)
            curr_lv = new_lv
            k-=1
        return [node.val for node in curr_lv]
