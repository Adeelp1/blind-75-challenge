# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def helper(root):
            if not root:
                return 0
            
            leftMax = helper(root.left)
            rightMax = helper(root.right)
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        
        helper(root)
        return res[0]

# TC : O(N)
# SC : O(H)