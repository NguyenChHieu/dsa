from collections import *
from heapq import *
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to create a binary tree from a list (level order insertion)
def create_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    for i, node in enumerate(nodes):
        if node is not None:
            if 2 * i + 1 < len(nodes):
                node.left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nodes):
                node.right = nodes[2 * i + 2]
    return nodes[0]

# Helper function to convert a binary tree to a list (level order traversal)
def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

def reverseOddLevels( root: Optional[TreeNode]) -> Optional[TreeNode]:
    curr_lv = 0
    lv = [root]

    while lv:
        new_lv = []
        tree_end = False

        if curr_lv % 2 == 1:
            # since complete binary tree so no need to check
            for node in lv:
                if not node.left: # no layers left
                    break
                new_lv.append(node.left)
                new_lv.append(node.right)
        else:
            node_vals = []
            for node in lv:
                if not node.left:
                    tree_end = True
                    break  # no layers left
                node_vals.append(node.left.val)
                node_vals.append(node.right.val)

            # Tree has no layers left
            if tree_end:
                break

            # reverse step
            i = len(node_vals) - 1
            for node in lv:
                node.left.val = node_vals[i]
                i -= 1
                node.right.val = node_vals[i]
                i -= 1
                new_lv.append(node.left)
                new_lv.append(node.right)
        lv = new_lv
        curr_lv += 1
    return root
t = create_tree([7,13,11])
print(tree_to_list(reverseOddLevels(t)))  #
new_t = reverseOddLevels(t)
print(tree_to_list(new_t))
