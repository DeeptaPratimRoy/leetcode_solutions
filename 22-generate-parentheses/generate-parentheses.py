class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def backtrack(open_count,close_count,subset):
            if len(subset) == 2*n:
                ans.append("".join(subset))
                return
            if open_count<n:
                subset.append("(")
                backtrack(open_count+1,close_count,subset)
                subset.pop()
            if close_count < open_count:
                subset.append(")")
                backtrack(open_count,close_count+1,subset)
                subset.pop()
        backtrack(0,0,[])
        return ans


        