class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        for n in nums:
            if i < 0:
                return False
            elif n > i:
                i = n
            i -= 1
        return True
    
# TC : O(N)
# SC : O(1)