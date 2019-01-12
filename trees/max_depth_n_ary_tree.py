# 559. Maximum Depth of N-ary Tree
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

def maxDepth(root):
    """
    :type root: Node
    :rtype: int
    """
    if root == None: return 0
    if len(root.children) == 0: return 1
    
    children_depths = [maxDepth(child) for child in root.children]
    return 1 + max(children_depths)

def max_depth_iterative(root):
    if root == None: return 0
            max_depth = 0
            queue = deque([ (root, 1) ])
            while queue:
                node, depth = queue.popleft()
                max_depth = max(max_depth, depth)
                for child in node.children:
                    queue.append(( child, depth + 1 ))
            return max_depth