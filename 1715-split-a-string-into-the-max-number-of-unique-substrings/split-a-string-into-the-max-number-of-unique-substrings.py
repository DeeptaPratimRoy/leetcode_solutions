
class Solution(object):
    def maxUniqueSplit(self, s):
        ans= [0]
        used = set()
        def backtrack(index):
            if index == len(s):
                ans[0] = max(ans[0],len(used))
            for end in range(index,len(s)):
                substring = s[index:end+1]
                if substring in used:
                    continue
                used.add(substring[:])
                backtrack(end+1)
                used.remove(substring)
        backtrack(0)
        return ans[0]

                

        