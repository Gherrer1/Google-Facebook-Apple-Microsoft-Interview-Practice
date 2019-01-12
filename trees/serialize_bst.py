# 449. Serialize and Deserialize BST
from collections import deque

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

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec2:
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
                
    def deserialize_helper(self, queue, min_val, max_val):
        if queue and min_val <= queue[0] and queue[0] <= max_val:
            node = TreeNode(queue.popleft())
            node.left = self.deserialize_helper(queue, min_val, node.val)
            node.right = self.deserialize_helper(queue, node.val, max_val)
            return node
        return None

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        
        nums = deque([int(num) for num in data.split(',')[:~0]])
        root = self.deserialize_helper(nums, float('-inf'), float('inf'))
        return root