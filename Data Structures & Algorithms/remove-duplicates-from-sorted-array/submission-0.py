class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l , r = 0, 1
        count = 0

        while (r < len(nums)):

            if nums[l] == nums[r]:
                r += 1
                count += 1
            else:
                temp = nums[l + 1]
                nums[l + 1] = nums[r]
                nums[r] = temp
                r += 1
                l += 1
        
        return len(nums) - count