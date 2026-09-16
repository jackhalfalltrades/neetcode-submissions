class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res =[]
        def dfs(stack, i, target):
            if target == 0:
                res.append(stack[::])
            if target <= 0 or i >= len(candidates):
                return
            
            stack.append(candidates[i])
            dfs(stack, i + 1, target - candidates[i])
            stack.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i = i + 1
            dfs(stack, i + 1, target)
        dfs([], 0, target)
        return res