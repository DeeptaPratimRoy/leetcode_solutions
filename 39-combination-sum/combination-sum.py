class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        def backtrack(curr_sum,index,subset):
            if curr_sum == target:
                ans.append(subset[:])
                return
            if curr_sum > target:
                return
            for i in range(index,len(candidates)):
                subset.append(candidates[i])
                backtrack(curr_sum+candidates[i],i,subset)
                subset.pop()
        backtrack(0,0,[])
        return ans

        