class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        freqNums = [[] for i in range(len(nums) + 1)]

        for n, c in count.items():
            freqNums[c].append(n)
        res = []
        for i in range(len(freqNums) - 1, -1 , -1):
            for n in freqNums[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    
