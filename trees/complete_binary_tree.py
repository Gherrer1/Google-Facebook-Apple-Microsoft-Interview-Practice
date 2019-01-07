from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.deque = deque([root])

        while True:
            parent = self.deque.popleft()
            if parent.left:
                self.deque.append(parent.left)
            if parent.right:
                self.deque.append(parent.right)
            else:
                self.deque.appendleft(parent)
                break
                
    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        parent = self.deque.popleft()
        if parent.left == None:
            parent.left = TreeNode(v)
            self.deque.appendleft(parent)
            self.deque.append(parent.left)
        elif parent.right == None:
            parent.right = TreeNode(v)
            self.deque.append(parent.right)
        return parent.val
        

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
