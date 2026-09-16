class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in dif:
                return [dif[d], i]
            dif[nums[i]] = i
        
