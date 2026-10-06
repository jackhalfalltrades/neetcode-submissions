class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charCount = {}

        for c in s:
            charCount[c] = 1 + charCount.get(c, 0)
        
        for c in t:
            if c not in charCount or charCount[c] == 0:
                return False
            charCount[c] = charCount[c] - 1
        return True
