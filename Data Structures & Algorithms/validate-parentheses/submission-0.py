class Solution:
    def isValid(self, s: str) -> bool:
        obj = {"}" : "{", ")" : "(", "]" : "["} 
        stack = []
        for c in s:
            if c not in obj:
                stack.append(c)
                continue
            if not stack or stack[-1] != obj[c]:
                return False
            stack.pop()
        return not stack