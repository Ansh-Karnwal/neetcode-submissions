class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_parent = {"}" : "{", ")" : "(", "]" : "["}
        for c in s:
            if c in valid_parent:
                if stack and stack[-1] == valid_parent[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack