class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxCon = 0
        while l < r:
            con = ((min(heights[l], heights[r])) * (r - l))
            maxCon = max(maxCon, con)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxCon