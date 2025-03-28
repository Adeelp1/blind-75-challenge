class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            if height[l] > height[r]:
                h = height[r]
                w = r - l
                area = h * w
                r -= 1
            else: 
                h = height[l]
                w = r - l
                area = h * w
                l += 1
            maxArea = max(area, maxArea)
        return maxArea
        

# TC : O(N)
# SC : O(1)