# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(t, s):
            if not t and not s:
                return True
            if not t or not s:
                return False
            
            if t.val != s.val:
                return False
            
            return isIdentical(t.left, s.left) and isIdentical(t.right, s.right)
        
        def helper(t, s):
            if not t:
                return False
            
            if isIdentical(t, s):
                return True
            return helper(t.left, s) or helper(t.right, s)
        
        return helper(root, subRoot)

# TC : O(N * M)
# SC : O(N + M)