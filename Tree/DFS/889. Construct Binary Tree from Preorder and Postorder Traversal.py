# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Key to solve this prob
    + No need to find the exact original tree that produce the lists, 
    just the one that has the preorder + postorder traversal matches the given.
    + Find the boundary which separates 2 subtrees
    """
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        N = len(preorder)
        postorder_save = {}
        for k, v in enumerate(postorder):
            postorder_save[v] = k

        def build(i1, i2, j1):
            # no nodes left
            if i1 > i2:
                return None
            
            root = TreeNode(preorder[i1])
            # > 2 nodes (still exist a subtree to be processed)
            if i1 != i2:
                boundary_left = preorder[i1+1]
                mid = postorder_save[boundary_left]
                # deduced from postorder, all the nodes from j1 to the boundary would be left subtree's
                left_st_size = mid - j1 + 1
                root.left = build(i1 + 1, i1 + left_st_size, j1)
                root.right = build(i1 + left_st_size + 1, i2, mid + 1)
            return root
        return build(0, N-1, 0)
