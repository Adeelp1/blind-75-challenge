class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        freq = defaultdict(int)
        N = len(s)
        min_len = N+1
        min_l = 0

        for ch in t:
            freq[ch] += 1
        
        required = len(freq)
        matches = 0

        for r in range(N):
            freq[s[r]] -= 1

            if freq[s[r]] == 0:
                matches += 1
            
            while required == matches:
                if (r-l+1) < min_len:
                    min_len = r-l+1
                    min_l = l
                
                if freq[s[l]] == 0:
                    matches -= 1
                
                freq[s[l]] += 1

                l += 1
        if min_len != N+1:
            return s[min_l:min_l+min_len]

        return ""

# TC : O(M+N)
# SC : O(alphabet)