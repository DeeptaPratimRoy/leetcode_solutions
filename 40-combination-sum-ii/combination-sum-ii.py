class Solution(object):
    def combinationSum2(self, candidates, target):
        ans= []
        candidates.sort()
        def backtrack(index,curr_sum,subset):
            if curr_sum == target:
                ans.append(subset[:])
                return
            if curr_sum > target:
                return
            for i in range(index,len(candidates)):
                if i > index and candidates[i-1] == candidates[i]:
                    continue
                subset.append(candidates[i])
                backtrack(i+1,curr_sum+candidates[i],subset)
                subset.pop()
        backtrack(0,0,[])
        return ans