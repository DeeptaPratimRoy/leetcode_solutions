class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(open_count, close_count, current):
            if len(current)==n*2:
                ans.append(current[:])
                return
            if open_count<n:
                backtrack(open_count+1,close_count,current+"(")
            if close_count<open_count:
                backtrack(open_count,close_count+1,current+")")
        backtrack(0,0,"")
        return ans