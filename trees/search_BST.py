# 700 on leetcode
def search_BST(self, root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    temp = root
    while temp:
        if temp.val == val:
            return temp
        elif val < temp.val:
            temp = temp.left
        else:
            temp = temp.right
    return None