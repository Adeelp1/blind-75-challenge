class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        c = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    c[i][j] = 1 + c[i+1][j+1]
                else:
                    c[i][j] = max(c[i][j+1], c[i+1][j])
        ans = c[i][j]
        return ans

# TC : O(N^2)
# SC : O(N^2)