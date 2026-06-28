class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        def backtrack(curr_sum, index, subset):
            if curr_sum == target:
                ans.append(subset[:])
                return
            if curr_sum > target:
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                backtrack(curr_sum + candidates[i], i + 1, subset)
                subset.pop()
        backtrack(0, 0, [])
        return ans