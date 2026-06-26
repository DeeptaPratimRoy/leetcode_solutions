class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def backtrack(open_count, close_count, current):    
            if len(current) == 2 * n:    
                ans.append("".join(current))    
                return    
            if open_count < n:    
                current.append("(")    
                backtrack(open_count + 1, close_count, current)    
                current.pop()    
            if close_count < open_count:    
                current.append(")")    
                backtrack(open_count, close_count + 1, current)    
                current.pop()    
        backtrack(0, 0, [])    
        return ans