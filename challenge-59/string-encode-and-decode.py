class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        size, res = [], ""

        for i in range(len(strs)):
            size.append(len(strs[i]))
        
        for s in size:
            res += str(s)
            res += ","
        
        res += "#"
        
        for i in range(len(strs)):
            res += strs[i]
        
        return res


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        size, i, res = [], 0, []

        while s[i] != "#":
            cur = ""

            while s[i] != ",":
                cur += s[i]
                i += 1
            size.append(int(cur))
            i += 1
        
        i += 1

        for sz in size:
            res.append(s[i: i + sz])
            i += sz
        
        return res

# TC : O(M)
# SC : O(M + N)