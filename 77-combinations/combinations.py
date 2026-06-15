class Solution(object):
    def combine(self, n, k):
        ans = []
        def backtrack(index,current):
            if len(current) == k:
                ans.append(current[:])
                return
            for i in range(index,n+1):
                current.append(i)
                backtrack(i+1,current)
                current.pop()
        backtrack(1,[])
        return ans
        