class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            
            visited.add(s[right])
            max_len = max(max_len, right - left+1)
        
        return max_len

# TC : O(N)
# SC : O(min(m, n))
# where m = len(s) and n = len(visited)