class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        retDict = defaultdict(list)
        for s in strs:
            charCount = [0] * 26
            for c in s:
                charCount[ord(c) - ord('a')] += 1
            retDict[tuple(charCount)].append(s)
        return list(retDict.values())

        