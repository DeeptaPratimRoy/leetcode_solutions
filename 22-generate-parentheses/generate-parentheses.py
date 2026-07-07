class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def backtrack(open,close,subset):
            if len(subset) == 2*n:
                ans.append("".join(subset))
            if open < n:    
                subset.append("(")    
                backtrack(open+ 1, close,subset)    
                subset.pop()    
            if close < open:    
                subset.append(")")    
                backtrack(open, close + 1, subset)    
                subset.pop()    
        backtrack(0, 0, [])    
        return ans

        