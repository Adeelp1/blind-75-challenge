class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1 = rob2 = 0
        for val in nums:
            decision = max(val + rob1, rob2)
            rob1 = rob2
            rob2 = decision

        return rob2

# TC : O(N)
# SC : O(1)