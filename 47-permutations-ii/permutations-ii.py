class Solution(object):
    def permuteUnique(self, nums):
        ans = []
        nums.sort()
        visited = [False]*len(nums)
        def backtrack(subset):
            if len(subset) == len(nums):
                ans.append(subset[:])
                return
            for i in range(len(nums)):
                if i > 0:
                    if visited[i-1] == False and nums[i] == nums[i-1]:
                        continue
                if visited[i] == False:
                    subset.append(nums[i])
                    visited[i] = True
                    backtrack(subset)
                    subset.pop()
                    visited[i] = False
        backtrack([])
        return ans


        