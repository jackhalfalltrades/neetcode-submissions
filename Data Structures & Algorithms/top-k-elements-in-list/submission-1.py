class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        for n in nums:
            numCount[n] = 1 + numCount.get(n, 0)
        freqNums = [[] for i in range(len(nums) + 1)]
        for n, c in numCount.items():
            freqNums[c].append(n)
        res = []
        for i in range(len(freqNums) - 1, -1 , -1):
            for n in freqNums[i]:
                res.append(n)
                if len(res) == k:
                    return res