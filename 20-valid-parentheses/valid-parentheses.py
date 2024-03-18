class Solution:
    def isValid(self, s: str) -> bool:
        corresponding = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in corresponding:
                stack.append(c)
                continue
            if not stack or stack[-1] != corresponding[c]:
                return False
            stack.pop()

        return not stack
