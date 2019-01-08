def get_sum(node, lower, upper):
    if node == None:
        return 0
    left_sum = 0
    node_val = 0
    right_sum = 0
    if node.left and node.val > lower:
        left_sum = get_sum(node.left, lower, upper)
    if node.right and node.val < upper:
        right_sum = get_sum(node.right, lower, upper)
    if lower <= node_val and node_val <= upper:
        node_val = node.val
    return left_sum + node_val + right_sum

def get_sum_iteratively(node, L, R):
    if node == None:
        return 0
    stack = [node]
    range_sum = 0
    while stack:
        n = stack.pop()
        if L <= n.val and n.val <= R:
            range_sum += n.val
        if n.left and n.val > lower:
            stack.append(n.left)
        if n.right and n.val < upper:
            stack.append(n.right)
    return range_sum