class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, stack, total):
            if total == target:
                res.append(stack.copy())
                return
            if i >= len(nums) or total > target:
                return
            stack.append(nums[i])
            dfs(i, stack, total + nums[i])
            stack.pop()
            dfs(i + 1, stack, total)
        dfs(0, [], 0)
        return res



        # def dfs(i, curr, total):
        #     if total == target:
        #         res.append(curr.copy())
        #         return
        #     if i>= len(nums) or total > target:
        #         return
        #     curr.append(nums[i])
        #     dfs(i, curr, total + nums[i])
        #     curr.pop()
        #     dfs(i + 1, curr, total)
        # dfs(0, [], 0)
        # return res