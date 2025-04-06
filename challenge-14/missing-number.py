class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        value = len(nums)

        for i, num in enumerate(nums):
            value ^= i ^ num
        return value

# TC : O(N)
# SC : O(1)