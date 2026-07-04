class Solution(object):
    def maxUniqueSplit(self, s):
        used = set()
        best = [0]
        def backtrack(index):
            if index == len(s):
                best[0] = max(best[0],len(used))
                return
            for end in range(index,len(s)):
                substring = s[index:end+1]
                if substring in used:
                    continue
                used.add(substring)
                backtrack(end+1)
                used.remove(substring)
        backtrack(0)
        return best[0]

                
                