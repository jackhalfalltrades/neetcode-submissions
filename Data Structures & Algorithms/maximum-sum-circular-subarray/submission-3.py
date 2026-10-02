class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        currMax, currMin, total = 0, 0, 0

        for n in nums:
            currMax = max(n, currMax + n)
            currMin = min(n, currMin + n)
            total += n
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)
        
        return max(total - globalMin, globalMax) if globalMax > 0 else globalMax