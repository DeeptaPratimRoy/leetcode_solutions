class Solution(object):
    def letterCombinations(self, digits):
        if digits == "":
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ans = []
        def backtrack(index,subset):
            if len(subset)==len(digits):
                ans.append(subset[:])
                return
            letters =  mapping[digits[index]]
            for letter in letters:
                backtrack(index+1,subset+letter)
        backtrack(0,"")
        return ans