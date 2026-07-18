class Solution(object):
    def permute(self, nums):
        nums.sort()
        ans = []
        visited = [False]*len(nums)
        def backtrack(subset):
            if len(subset) == len(nums):
                ans.append(subset[:])
                return
            for i in range(len(nums)):
                if visited[i] == False:
                    subset.append(nums[i])
                    visited[i] = True
                    backtrack(subset)
                    subset.pop()
                    visited[i] = False
        backtrack([])
        return ans


                    