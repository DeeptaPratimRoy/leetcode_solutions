class Solution(object):
    def combinationSum(self, candidates, target):
        ans =[]
        def backtrack(index,curr_sum,subset):
            if curr_sum == target:
                ans.append(subset[:])
                return
            if curr_sum>target:
                return
            for i in range(index,len(candidates)):
                subset.append(candidates[i])
                backtrack(i,curr_sum+candidates[i],subset)
                subset.pop()
        backtrack(0,0,[])
        return ans


        