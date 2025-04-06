class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        
        for i in range(n - 2, -1, -1):
            c = a+b
            a = b
            b = c
        return b
        
# TC : O(N)
# SC : O(1)