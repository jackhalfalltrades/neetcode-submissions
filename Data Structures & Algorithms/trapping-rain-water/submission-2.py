class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        waterArea = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                waterArea += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                waterArea += rightMax - height[r]
        return waterArea