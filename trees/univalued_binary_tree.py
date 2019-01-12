# 965
from collections import deque
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def is_univalue_tree(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root == None or (root.left == None and root.right == None):
        return True
    if root.left and root.left.val != root.val:
        return False
    if root.right and root.right.val != root.val:
        return False
    return is_univalue_tree(root.left) and is_univalue_tree(root.right)

def is_univalue_tree_bfs(root):
    if root == None:
        return True
    queue = deque([ root ])
    while queue:
        node = queue.popleft()
        if node == None: continue
        if node.left and node.left.val != node.val:
            return False
        if node.right and node.right.val != node.val:
            return False
        queue.apppend(node.left)
        queue.append(node.right)
    return True