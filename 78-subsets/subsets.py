class Solution(object):
    def subsets(self, nums):
        ans= []
        def backtrack(index,subsets):
            if index == len(nums):
                ans.append(subsets[:])
                return
            subsets.append(nums[index])
            backtrack(index+1,subsets)
            subsets.pop()
            backtrack(index+1,subsets)
        backtrack(0,[])
        return ans
