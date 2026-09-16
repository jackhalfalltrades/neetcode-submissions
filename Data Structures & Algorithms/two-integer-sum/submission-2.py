class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numset:
                return [numset[diff], i]
            else:
                numset[n] = i
