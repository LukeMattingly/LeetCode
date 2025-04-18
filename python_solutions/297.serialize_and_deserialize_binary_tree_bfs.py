from typing import List, Optional
import unittest
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if not node:
                return result.append("null")
            
            result.append(str(node.val))
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return ",".join(result)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0
        if vals[self.i] == "null":
            self.i +=1
            return None
        
        root = TreeNode(int(vals[self.i]))
        self.i +=1
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if vals[self.i] != "null":
                node.left = TreeNode(int(vals[self.i]))
                queue.append(node.left)
            self.i+=1
            if vals[self.i] != "null":
                node.right = TreeNode(int(vals[self.i]))
                queue.append(node.right)
            self.i+=1
        return root



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


if __name__ == '__main__':
    unittest.main()