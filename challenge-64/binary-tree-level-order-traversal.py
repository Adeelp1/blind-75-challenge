# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def bfs(c_node):
            if not c_node:
                return []
            q = deque()
            q.append(c_node)

            while q:
                n = len(q)
                temp = []
                for _ in range(n):
                    node = q.popleft()
                    temp.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(temp)
        bfs(root)

        return res

# TC : O(N)
# SC : O(N)