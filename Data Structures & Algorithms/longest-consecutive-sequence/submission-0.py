class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in numSet:
                length = 0
                while nums[i] + length in numSet:
                    length += 1
                res = max(res, length)
        return res

