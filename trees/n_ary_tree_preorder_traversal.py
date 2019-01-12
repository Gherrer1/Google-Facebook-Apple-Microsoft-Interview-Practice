# 589. N-ary Tree Preorder Traversal
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

def preorder_recursive(root):
    """
    :type root: Node
    :rtype: List[int]
    """
    if root == None: return []
    traversal = [root.val]
    for child in root.children:
        traversal.extend(preorder_recursive(child))
    return traversal

def preorder(root):
    """
    :type root: Node
    :rtype: List[int]
    """
    if root == None:
        return []
    ret_val = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node == None: continue
        ret_val.append(node.val)
        num_children = len(node.children)
        for i in xrange(num_children):
            stack.append(node.children[num_children - 1 - i])
    return ret_val
        
testTree1 = Node(
    1,
    [
        Node(
            3,
            [
                Node(5, []),
                Node(6, [])
            ]
        ),
        Node(2, []),
        Node(4, [])
    ]
)

print preorder_recursive(None)
print preorder_recursive(testTree1) # [1, 3, 5, 6, 2, 4]
print preorder_recursive(None) # []