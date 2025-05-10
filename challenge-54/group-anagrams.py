class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            s_char = "".join(sorted(word))
            if s_char not in d:
                d[s_char] = [word]
            else:
                d[s_char].append(word)
    

        return list(d.values())

# TC : O(N * K Log K)
# SC : O( N * K)