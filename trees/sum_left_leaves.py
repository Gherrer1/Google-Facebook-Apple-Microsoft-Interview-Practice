# solution 1: recursion
def sum_left_leaves1(node, leaf_sum=0):
    if node == None:
        return 0
    if node.left:
        if node.left.left == None and node.left.right == None:
            leaf_sum += node.left.val
        else:
            leaf_sum = sum_left_leaves(node.left, leaf_sum)
    if node.right:
        leaf_sum = sum_left_leaves(node.right, leaf_sum)
    return leaf_sum

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution 2: stack
def sum_left_leaves(node):
    if node == None: return 0
    leaf_sum = 0
    stack = [node]
    while stack:
        n = stack.pop()
        if n.right:
            stack.append(n.right)
        if n.left:
            if n.left.left == None and n.left.right == None:
                leaf_sum += n.left.val
            else:
                stack.append(n.left)
    return leaf_sum


tree = Node(3,
    Node(9),
    Node(20,
        Node(15),
        Node(7)
    )
)

tree2 = Node(6)

print sum_left_leaves(tree) # expect 24
print sum_left_leaves(tree2) # expect 0
print sum_left_leaves(None) # expect 0

tree3 = Node(25,
    Node(10),
    Node(15, right=Node(26, right=Node(30, right=Node(45, right=Node(60, right=Node(80, Node(100)))))))
)

print sum_left_leaves(tree3) # expect 110