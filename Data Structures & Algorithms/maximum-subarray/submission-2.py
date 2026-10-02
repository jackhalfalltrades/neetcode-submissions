class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxSum = nums[0]
        currSum = 0

        if len(nums) < 2:
            return maxSum

        MAX_L, MAX_R = 0, 0
        L = 0

        for R in range(len(nums)):
            if currSum < 0:
                currSum = 0
                L = R
            currSum += nums[R]
            maxSum = max(maxSum, currSum)
            MAX_L, MAX_R = L,R
        return maxSum



        # for n in nums:
        #     currSum = max(currSum, 0)
        #     currSum += n
        #     maxSum = max(maxSum, currSum)
        # return maxSum