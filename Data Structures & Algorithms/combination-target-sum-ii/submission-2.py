class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res =[]
        def dfs(stack, i, total):
            if total == 0:
                res.append(stack[::])
            if i >= len(candidates) or total <= 0:
                return
            stack.append(candidates[i])
            dfs(stack, i + 1, total - candidates[i])
            stack.pop()
            while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(stack, i + 1, total)
        dfs([], 0, target)
        return res
        