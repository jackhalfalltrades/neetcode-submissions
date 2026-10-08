class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        total = 0
        for i, n in enumerate(nums):
            prefix[i] += total
            total += n

        total = 0
        for i in range(len(nums) -1, -1, -1):
            postfix[i] += total
            total += nums[i]
        
        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i
        return -1

        

