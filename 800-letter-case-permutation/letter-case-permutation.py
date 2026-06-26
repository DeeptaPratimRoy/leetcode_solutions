class Solution(object):
    def letterCasePermutation(self, s):
        ans = []
        def backtrack(index,subset):
            if index == len(s):
                ans.append("".join(subset[:]))
                return

            if s[index].isalpha():
                subset.append(s[index].lower())
                backtrack(index+1,subset)
                subset.pop()
                subset.append(s[index].upper())
                backtrack(index+1,subset)
                subset.pop()
            else:
                subset.append(s[index])
                backtrack(index+1,subset)
                subset.pop()
        backtrack(0,[])
        return ans
                
                