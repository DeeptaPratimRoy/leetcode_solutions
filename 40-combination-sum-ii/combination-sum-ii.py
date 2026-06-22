class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        def backtrack(current,curr_sum,subset):
            if curr_sum == target:
                ans.append(subset[:])
                return
            if curr_sum > target:
                return
            for i in range(current,len(candidates)):
                if i > current and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                backtrack(i+1,curr_sum+candidates[i],subset)
                subset.pop()
        backtrack(0,0,[])
        return ans

        