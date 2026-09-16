class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(stack, i, total):
            if total == target:
                res.append(stack[::])
                return
            if i >= len(nums) or total > target:
                return
            stack.append(nums[i])
            dfs(stack, i, total + nums[i])
            stack.pop()
            dfs(stack, i + 1, total)
        dfs([], 0, 0)
        return res