# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root :
            return ""

        self.ans = []

        def traversal(node):
            if node == None:
                self.ans.append("null")
                return
            self.ans.append(str(node.val))
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return ",".join(self.ans)        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return []
        self.arr = data.split(",")

        def create():
            if not self.arr:
                return None
            val = self.arr.pop(0)

            if val == "null":
                return None
            
            Node = TreeNode(val)
            Node.left = create()
            Node.right = create()

            return Node
        return create()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# TC : O(N)
# SC : O(N)