class Solution(object):
    def combinationSum3(self, k, n):
        ans = []
        def backtrack(curr_sum,index,subset):
            if len(subset) == k:
                if curr_sum == n:
                    ans.append(subset[:])
                    return
            if curr_sum> n:
                return
            for i in range(index,10):
                subset.append(i)
                backtrack(curr_sum+i,i+1,subset)
                subset.pop()
        backtrack(0,1,[])
        return ans


        
        