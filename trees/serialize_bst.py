# 449. Serialize and Deserialize BST
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ''
        stack = [root]
        ret_val = ''
        SEP = ','
        while stack:
            node = stack.pop()
            ret_val += (str(node.val) + SEP)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ret_val
    
    def insert(self, root, num):
        temp = root
        while True:
            if num > temp.val:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = TreeNode(num)
                    return
            else:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = TreeNode(num)
                    return

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        
        nums = data.split(',')
        root = None
        for i in range(len(nums) - 1):
            num = int(nums[i])
            if root == None:
                root = TreeNode(num)
            else:
                self.insert(root, num)
        return root