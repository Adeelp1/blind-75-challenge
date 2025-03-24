class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = 1
        cur_max = 1
        res = nums[0]

        for num in nums:
            temp = cur_max * num
            cur_max = max(temp, cur_min * num, num)
            cur_min = min(temp, cur_min * num, num)

            res = max(res, cur_max)
        
        return res

        