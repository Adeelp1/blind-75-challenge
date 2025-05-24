# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, minval, maxval):
            if not node:
                return True
            
            if not(minval < node.val < maxval):
                return False
            
            left_bst = check(node.left, minval, node.val)
            right_bst = check(node.right, node.val, maxval)
            return left_bst and right_bst
        
        return check(root, float("-inf"), float("inf"))

# TC : O(N)
# SC : O(N)