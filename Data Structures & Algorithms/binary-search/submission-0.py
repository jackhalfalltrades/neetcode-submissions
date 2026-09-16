class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        return self.binary_search(left, right, nums, target)

    def binary_search(self, l, r, nums, target) -> int:
        if l > r:
            return -1
        m = l + (r- l) // 2
        if nums[m] == target:
            return m;
        if nums[m] < target:
            return self.binary_search(m+1, r, nums, target)
        return self.binary_search(l, m - 1, nums, target)


