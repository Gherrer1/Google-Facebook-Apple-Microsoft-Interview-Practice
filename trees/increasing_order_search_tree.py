class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def inorder(root):
    if root.left:
        inorder(root.left)
    print root.val
    if root.right:
        inorder(root.right)

def push_all(stack, node):
    temp = node
    while temp:
        stack.append(temp)
        temp = temp.left

def get_increasing_tree(root):
    if root == None:
        return None
    stack = []
    push_all(stack, root)
    new_root = stack[~0]
    temp = None
    while stack:
        node = stack.pop()
        if temp:
            temp.right = node
        temp = node
        node.left = None
        if node.right:
            push_all(stack, node.right)
    return new_root

def get_increasing_tree_recursive(root):
    if root == None:
        return None, None
    l_root, temp = get_increasing_tree_recursive(root.left)
    if temp:
        temp.right = root
    if not l_root:
        l_root = root
    temp = root
    root.left = None
    r_root, r_tail = get_increasing_tree_recursive(root.right)
    if r_root:
        temp.right = r_root
        temp = r_tail
        # do some connecting
    return (l_root, temp)


testTree = TreeNode(
    5,
    TreeNode(3,
        TreeNode(2,
            TreeNode(1)
        ),
        TreeNode(4)
    ),
    TreeNode(6,
        None,
        TreeNode(8,
            TreeNode(7),
            TreeNode(9)
        )
    )
)

# testTree = get_increasing_tree(testTree)

inorder(testTree)