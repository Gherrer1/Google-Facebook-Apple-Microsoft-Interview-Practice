# note: problem came with caveats
# 1. tail will never be deleted
# 2. node input will always be valid
# 3. every node in the LL will have a unique value
# 4. LL will be at least 2 elements
# 5. You are only given access to the node you want to delete
def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next