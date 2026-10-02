class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxSum = nums[0]
        currSum = 0

        if len(nums) < 2:
            return maxSum

        for n in nums:
            currSum = max(currSum, 0)
            currSum += n
            maxSum = max(maxSum, currSum)
        return maxSum