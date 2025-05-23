# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        mapping = {}

        for i in range(len(preorder)):
            mapping[inorder[i]] = i

        def create(s, e):
            if s > e: return None

            root = TreeNode(preorder.popleft())
            m = mapping[root.val]
            root.left = create(s, m-1)
            root.right = create(m+1, e)
            return root

        return create(0, len(preorder)-1)
    
# TC :O(N)
# SC :O(N)