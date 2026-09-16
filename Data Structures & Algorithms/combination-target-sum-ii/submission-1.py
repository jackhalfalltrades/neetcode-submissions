class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, stack, total):
            if total == 0:
                res.append(stack.copy())
                
            if i >= len(candidates) or total <= 0:
                return
            stack.append(candidates[i])
            dfs(i + 1 , stack, total - candidates[i])
            stack.pop()
            while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1 , stack, total)
        dfs(0, [], target)
        return res