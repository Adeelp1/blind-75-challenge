class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        op = { "[", "{", "(" }

        for i in range(len(s)):
            if s[i] in op:
                stack.append(s[i])
            else:
                if not stack \
                or stack[-1] != "{" and  s[i] == "}" \
                or stack[-1] != "[" and  s[i] == "]" \
                or stack[-1] != "(" and  s[i] == ")":
                    return False
                stack.pop()
    

        return not stack

# TC : O(N)
# SC : O(N)