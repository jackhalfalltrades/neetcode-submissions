class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = set()

        for i in range(len(nums)):
            d = target - nums[i]
            if d in numSet:
                return [nums.index(d), i]
            else:
                numSet.add(nums[i])
        