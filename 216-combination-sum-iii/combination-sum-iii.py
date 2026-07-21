class Solution(object):
    def combinationSum3(self, k, n):
        ans = []
        def backtrack(index,curr_sum,subset):
            if len(subset) == k:
                if curr_sum == n:
                    ans.append(subset[:])
                    return
            if curr_sum > n:
                return
            for i in range(index,10):
                subset.append(i)
                backtrack(i+1,curr_sum+i,subset)
                subset.pop()
        backtrack(1,0,[])
        return ans
            
