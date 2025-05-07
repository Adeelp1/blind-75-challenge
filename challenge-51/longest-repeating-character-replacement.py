class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        left = 0
        counts = [0] * 26

        for right in range(len(s)):
            counts[ord(s[right]) - 65] += 1

            while (right-left+1) - max(counts) > k:
                counts[ord(s[left]) - 65] -= 1
                left += 1
            
            max_count = max(max_count, (right-left+1))
        
        return max_count

# TC : O(N)
# SC : O1