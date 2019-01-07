# 144 on leetcode
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def preorder_traversal(root):
    if root == None:
        return []
    res = [root.val]
    if root.left:
        res += preorder_traversal(root.left)
    if root.right:
        res += preorder_traversal(root.right)
    return res

def preorder_traversal_iterative(root):
    if root == None:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

tree = TreeNode(
    1,
    None,
    TreeNode(
        2,
        TreeNode(3)
    )
)

print preorder_traversal(tree)
print preorder_traversal_iterative(tree)