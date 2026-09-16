class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0: return False

        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        
        return max(counter.values()) > 1