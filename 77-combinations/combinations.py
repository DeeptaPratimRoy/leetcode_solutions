class Solution(object):
    def combine(self, n, k):
        ans = []
        def backtrack(start,subset):
            if len(subset) == k:
                ans.append(subset[:])
                return ans
            for i in range(start,n+1):
                subset.append(i)
                backtrack(i+1,subset)
                subset.pop()
        backtrack(1,[])
        return ans


        