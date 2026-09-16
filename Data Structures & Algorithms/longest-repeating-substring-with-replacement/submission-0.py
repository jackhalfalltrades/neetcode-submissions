class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxFreq = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxFreq = max(maxFreq, freq[s[r]])
            if(r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
        return (r - l + 1)
