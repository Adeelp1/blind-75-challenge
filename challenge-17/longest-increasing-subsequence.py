class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l = len(nums)
        dp = [1] * l

        for i in range(1, l):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

# TC : O(N^2)
# SC : O(N)