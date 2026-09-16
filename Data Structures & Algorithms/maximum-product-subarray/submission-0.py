class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        prevProduct = 1
        for n in nums:
            curProduct = prevProduct * n
            res = max(res, max(curProduct, n))
            prevProduct = curProduct
        return res

