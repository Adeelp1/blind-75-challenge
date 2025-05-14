class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(s, l, r, c = 0):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                c += 1
            return c
        
        count = 0

        for i in range(len(s)):
            even = expand(s, i, i+1)
            odd = expand(s, i, i)

            count += even + odd
        
        return count

# TC : O(N^2)
# SC : O(1)