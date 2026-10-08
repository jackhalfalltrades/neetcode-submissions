class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * len(nums)
        total = 0
        for i, n in enumerate(nums):
            total += n
            self.prefix[i] += total
        

    def sumRange(self, left: int, right: int) -> int:
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return preRight - preLeft
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)