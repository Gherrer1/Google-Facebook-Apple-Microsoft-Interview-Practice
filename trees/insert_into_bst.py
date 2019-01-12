# 701. Insert into a Binary Search Tree
def insert_into_bst(root, val):
    if root == None: return TreeNode(val)
            
            temp = root
            while temp:
                if val > temp.val:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right = TreeNode(val)
                        return root
                elif val < temp.val:
                    if temp.left:
                        temp = temp.left
                    else:
                        temp.left = TreeNode(val)
                        return root
# recursive
def insert_into_bst_recursive(root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    if root == None: return TreeNode(val)
    
    if val > root.val:
        if root.right:
            insert_into_bst_recursive(root.right, val)
        else:
            root.right = TreeNode(val)
            return root
    else:
        if root.left:
            insert_into_bst_recursive(root.left, val)
        else:
            root.left = TreeNode(val)
            return root
    return root
